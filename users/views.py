from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Log out view
def logout_view(request):
    """ loging user out """
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register(request):
    """ creating new user """
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # upload compleated form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log user in and redirect 
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('uni_notes:topic_list'))
    context = {'form':form}
    return render(request, 'users/register.html', context)            
