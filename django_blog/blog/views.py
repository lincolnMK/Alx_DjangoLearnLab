from django.shortcuts import render, redirect
from django.contrib.auth import login

from blog.models import Post
from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages





def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You are now logged in.")
            messages.error(request, "An error occurred during registration. Please try again.")
            login(request, user)  # auto-login after registration
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "blog/register.html", {"form": form})


from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

@login_required
def profile_view(request):
    """
    Display the profile of the currently logged-in user
    """
    user = request.user
    profile = getattr(user, 'profile', None)  # in case you have a Profile model

    context = {
        'user': user,
        'profile': profile
    }

    return render(request, 'profile_view.html', context)
