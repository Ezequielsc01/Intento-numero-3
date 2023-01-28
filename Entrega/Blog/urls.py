from Blog import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path ('Login/', views.login_request , name='login' ),
    path ('Register/', views.register , name='register'),
]