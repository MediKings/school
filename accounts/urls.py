from django.urls import path
from .views import Logout, Register, Login, ProfileView, UpdateProfile

app_name='accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('profile/<int:pk>', ProfileView, name='profile'),
    path('update_profile/<int:pk>', UpdateProfile, name='update_profile'),
]