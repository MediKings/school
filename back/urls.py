from django.urls import path
from .views import Dashboard, Authors, AddUniv

app_name='back'

urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'),
    path('authors/', Authors, name='authors'),
    path('add/univ/', AddUniv.as_view(), name='add-univ'),
]