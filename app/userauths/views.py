from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_view(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST or none)
		if form.is_valid():
			new_user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Olá {username}, sua conta foi criada com sucesso!')

			# Automatic login after registration
			new_user = authenticate(username=form.cleaned_data['email'],
									password=form.cleaned_data['password1'],
			)
			login(request, new_user)

	else:
		form = UserRegisterForm()

	context = {
	'form': form
	}

	return render(request, 'userauths/sign-up.html', context)
