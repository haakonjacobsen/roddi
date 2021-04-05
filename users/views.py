from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .forms import UserRegisterForm, VoteForm
from dodsbo.models import Item, Estate, Participate, Wish, Favorite, Alert, Comment
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect



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


def checkAlert(user, estate):
    check = False
    alerts = list(Alert.objects.all())
    for alert in alerts:
        if alert.estateID == estate and alert.user == user:
            check = True
    return check


class ProfileListView(ListView):
    template_name = 'users/profile.html'
    model = Estate

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        # returnerer alt for admin siden
        if current_user.is_staff:
            #estate_info = [[Estate.object, [[User, percentage],[User, percentage]]],[Estate.object, [User, percentage]]]
            estate_stats = []
            all_estates = Estate.objects.all()
            User = get_user_model()
            estates = []
            for estate in all_estates:
                #get members
                participate = Participate.objects.filter(estateID=estate).values_list('username', flat=True)
                members = User.objects.filter(pk__in=participate)
                #get item stats
                items_in_estate = Item.objects.filter(estateID=estate).values_list('pk', flat=True)
                wishes_in_estate = Wish.objects.filter(itemID__in=items_in_estate)
                members_stat = []
                sum_votes = 0
                for member in members:
                    member_votes = wishes_in_estate.filter(username=member).count()
                    members_stat.append([member, member_votes])
                    sum_votes += member_votes
                if (len(members)>0 and len(items_in_estate)>0):
                    percentage_done = int(sum_votes/len(members)/len(items_in_estate)*100)
                else:
                    percentage_done = "100"
                estates.append([estate, members_stat,len(items_in_estate), percentage_done])
            context['estates'] = estates
            return context
        # returnerer alt for bruker siden
        else:
            participate_list = list(
                Participate.objects.filter(username=current_user))
            estates = []
            for participate in participate_list:
                estate = participate.estateID
                part_memb_list = list(Participate.objects.filter(estateID=estate))
                estate_members = []
                for par in part_memb_list:
                    estate_members.append(par.username)
                estates.append([estate, estate_members])

            context['estates'] = estates
            context['me'] = Alert.objects.filter(user=current_user)
        return context


class EstateDetailView(DetailView):
    template_name = 'users/estate.html'
    model = Estate

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # if(len(Participate.objects.filter(username=self.request.user, estateID=self.object)) > 0):
        return super(EstateDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        item_list = list(Item.objects.filter(estateID=self.object))
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

        context['assets'] = user_items
        return context


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
def new_vote(request):
    form = VoteForm(request.POST or None)
    if request.method == "POST":
        form = VoteForm(request.POST)
        current_user = request.user
        post_itemID = request.POST.get('itemID')
        item = Item.objects.filter(id=post_itemID).first()
        estate_id = item.estateID.pk
        item_list = list(Item.objects.all())
        clicked_item = None
        for item in item_list:
            if item.id == post_itemID:
                clicked_item = item
        choice = request.POST.get('btn')
        wish, created = Wish.objects.get_or_create(
            itemID_id=post_itemID, username=current_user)
        wish.choice = choice
        wish.full_clean(exclude=None, validate_unique=True)
        wish.save()
    else:
        form = VoteForm()

    return HttpResponseRedirect("/estate/{id}/".format(id=estate_id))


def favorite_item(request):
    user = request.user
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_object = Item.objects.get(id=item_id)
        estate_id = item_object.estateID.pk
        if user in item_object.Favorite.all():
            item_object.Favorite.remove(user)
        else:
            item_object.Favorite.add(user)

        like, created = Favorite.objects.get_or_create(
            username=user, itemID_id=item_id)

        if not created:
            if like.favorite == 'Ønsket':
                like.favorite = 'Angre ønsket'
            else:
                like.favorite = 'Ønsket'
        like.save()

    return HttpResponseRedirect("/estate/{id}/".format(id=estate_id))


def comment(request, pk):
    item_pk = pk
    item_comments = Comment.objects.all()
    comments = []
    name = ""
    for c in item_comments:
        if c.itemID_id == item_pk:
            comments.insert(0, c)
            name = comments[0].itemID.name
    context = {
        'comments': comments,
        'name': name
    }

    return render(request, 'users/comments.html', context)


class AddCommentView(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'users/comment_form.html'

    def form_valid(self, form):
        form.instance.itemID_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('comments', kwargs={'pk': self.kwargs['pk']})
