from django.urls import path

from .views.register import register_view
from .views.login import login_view
from .views.logout import logout_view

app_name = "account"

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]