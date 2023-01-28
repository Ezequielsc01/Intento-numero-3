from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post
from django import forms
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'Blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'Blog/post_detail.html', {'post': post, 'form': form})


def register(request):
      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"BlogFinal/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"BlogFinal/registro.html" ,  {"form":form})


def login_request(request):
      

      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():  # Si pasó la validación de Django

                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')

                  user = authenticate(username= usuario, password=contrasenia)

                  if user is not None:
                        login(request, user)

                        return render(request, "BlogFinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
                  else:

                        form = AuthenticationForm()   
                        return render(request, "BlogFinal/login.html", {"mensaje":"Datos incorrectos"}, {"form": form})
         


            else:

                  form = AuthenticationForm()   
                  return render(request, "BlogFinal/login.html"  , {"form": form, "mensaje" : "Datos incorrectos"})
                  


      form = AuthenticationForm()

      return render(request, "BlogFinal/login.html", {"form": form})