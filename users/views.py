from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import UserRegisterForm, CommentForm
from dodsbo.models import Item, Estate, Participate, Comment


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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


@login_required
def items(request):
    current_user = request.user
    items = list(Item.objects.all())
    estates = []
    for par in Participate.objects.all():
        if par.username == current_user:
            estates.append(par.estateID)
    user_items = []
    for item in items:
        if item.estateID in estates:
            user_items.append(item)
    context = {
        'assets': user_items
    }
    return render(request, 'users/items.html', context)


def comment(request, pk):
    item_pk = pk
    item_comments = Comment.objects.all()
    comments = []
    for c in item_comments:
        if c.itemID_id == item_pk:
            comments.append(c)
    context = {
        'comments': comments
    }

    return render(request, 'users/comments.html', context)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'users/add_comment.html'


    def form_valid(self, form):
        form.instance.itemID_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('items')
