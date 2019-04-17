from django.urls import path

from .views import GetMemes

urlpatterns = [
    path('memes/', GetMemes.as_view(), name="memes-all")

]