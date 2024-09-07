from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',login,name='login'),
    path('index',index,name='index'),
    path("register/",register,name = "register"),
    path("add_user/",add_user,name = "add_user"),
    path("check/",check,name = "check"),
    path("logout/",logout,name="logout"),
    path('login',login,name="login"),
    path("save/",save,name="save"),
    path("delete/<str:id>",delete, name="delete"),
    path("edit/<str:id>",edit,name = "edit")
    # path('update_user/<int:id>',update_user,name='update_user')
]