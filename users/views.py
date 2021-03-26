from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .forms import UserRegisterForm
from dodsbo.models import Item, Estate, Participate


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


class ProfileListView(ListView):
    template_name = 'users/profile.html'
    model = Estate

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = self.request.user
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
        return context


class EstateDetailView(DetailView):
    template_name = 'dodsbo/estate.html'
    model = Estate

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # if(len(Participate.objects.filter(username=self.request.user, estateID=self.object)) > 0):
        return super(EstateDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Items'] = Item.objects.filter(estateID=self.object)
        return context
