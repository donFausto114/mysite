from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class Homepage(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/start_page.html')

def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			user = authenticate(username=username,password=password)
			login(request,user)
			messages.success(request, ("Registration Success!"))
			return redirect("main:homepage")
	else:
		form = UserCreationForm()
	return render(request, "auth/register_user.html", {"form":form})