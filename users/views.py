from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required  # Krever at man må være logget inn for å aksessere siden
def profile(request):
    current_user = request.user
    participate_list = list(Participate.objects.filter(username=current_user))
    estates = []
    for participate in participate_list:
        estate = participate.estateID
        print(estate)
        part_memb_list = list(Participate.objects.filter(estateID=estate))
        estate_members = []
        for par in part_memb_list:
            estate_members.append(par.username)
        estates.append([estate, estate_members])
    for i in range(0, len(estates), 2):
        print(estates[i])
    context = {
        # gjenstand funker som nøkkel til kodeblokken i home.html
        'estates': estates

    }
    return render(request, 'users/profile.html', context)
