from django.http import HttpResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *



menu = [ { 'title': "О сайте", 'url_name': 'about'},
{'title': "Добавить книгу", 'url_name': 'add_page'},
{'title': "Обратная связь", 'url_name': 'contact'},
{ 'title': "Войти", 'url_name': 'login' }
  ]

 
def index(request):
	posts = Boocks.objects.all()
	context = {
		'posts': posts,
		'menu': menu,
		'title': 'Главная страница'
	}
	return render(request, 'boocks/index.html', context=context)

def about(request):

	context = {
		'menu': menu,
		'title': 'О сайте'
	}

	return render(request, 'boocks/about.html', context=context)

def addpage(request):
	return HttpResponse("Добавление книги")

def contact(request):
	return HttpResponse("Обратная связь")

def login(request):
	return HttpResponse("Авторизация")


def Show_Boocks(request, boocks_id):
	return HttpResponse(f"<h1> Книги по категориям </h1> <p>{boocks_id}</p>")
