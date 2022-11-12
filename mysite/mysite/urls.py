# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from authzolk import views

urlpatterns = [
    path("chat", views.chat, name="chat"),
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
]
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('register', views.register, name='register'),
#     path('<str:room_name>/', views.room, name='room'),
#     path('chat', views.chat, name='chat'),
#     path('logout', views.logoutUser, name='logout'),
# ]
