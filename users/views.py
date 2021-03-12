from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, VoteForm
from dodsbo.models import Item, Estate, Participate, Wish


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(
                request, f'Registrering var vellykket, du kan nå logge inn!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required  # Krever at man må være logget inn for å aksessere siden
def profile(request):
    current_user = request.user
    participate_list = list(Participate.objects.filter(username=current_user))
    estates = []
    for participate in participate_list:
        estate = participate.estateID
        part_memb_list = list(Participate.objects.filter(estateID=estate))
        estate_members = []
        for par in part_memb_list:
            estate_members.append(par.username)
        estates.append([estate, estate_members])
    context = {
        # gjenstand funker som nøkkel til kodeblokken i home.html
        'estates': estates

    }
    return render(request, 'users/profile.html', context)


def load_items(request):
    current_user = request.user
    item_list = list(Item.objects.all())
    estates = []
    for par in Participate.objects.all():
        if par.username == current_user:
            estates.append(par.estateID)
    user_items = []
    for item in item_list:
        if item.estateID in estates:
            choice, wish = checkWish(current_user, item)
            item.check = choice
            user_items.append(item)
    return user_items

def checkWish(user, item):
    wishes = list(Wish.objects.all())
    choiceInt = -1
    wishID = -1
    for wish in wishes:
        if wish.username.username == user.username and wish.itemID == item:
            choiceInt = wish.choice
            wishID = wish.id
    return choiceInt, wishID


@login_required
def items(request):
    context = {
        'assets': load_items(request)
    }
    return render(request, 'users/items.html', context)

@login_required
def vote(request):
    form = VoteForm(request.POST or None)
    if request.method == "POST":
        form = VoteForm(request.POST)
        current_user = request.user
        post_itemID = request.POST.get('itemID')
        item_list = list(Item.objects.all())
        clicked_item = None
        for item in item_list:
            if item.id == post_itemID:
                clicked_item = item
        prev_choice, id = checkWish(current_user, clicked_item)
        choice = request.POST.get('btn')
        print("choice: " + choice)
        if prev_choice != -1: #dette funker ikke 
            Wish.objects.filter(id=id).delete()
        wish = Wish.objects.create(itemID=item, username=current_user, choice=choice)
        wish.full_clean(exclude=None, validate_unique=True)
        wish.save()

    else:
        form = VoteForm()

    context = {
        'assets': load_items(request)
    }

    return render(request, 'users/items.html', context)
