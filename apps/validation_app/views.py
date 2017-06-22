# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, 'validation_app/index.html')

def process(request):
	print "*"*50
	print request.POST['user_name']
	print "*"*50
	post_data = request.POST['user_name']
	print "*"*50
	print post_data
	print "*"*50
	result = User.objects.validate(post_data)
	if isinstance(result, list):
		for err in result:
			messages.add_message(request, messages.ERROR, err)
		return redirect('/')
	else:
		request.session['user'] = request.POST['user_name']
		return redirect('/success')
	return redirect('/')
def success(request):
	usernames = User.objects.all()
	context = {
		'user': request.session['user'],
		'users': usernames
	}
	return render(request, 'validation_app/success.html', context)
