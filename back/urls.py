from django.urls import path
from .views import Dashboard, Authors, AddUniv, UpdateUniv, DeleteUniv

app_name='back'

urlpatterns = [
    path('dashboard/', Dashboard, name='dashboard'),
    path('authors/', Authors, name='authors'),
    path('add_univ/', AddUniv.as_view(), name='add_univ'),
    path('update_univ/<slug:slug>/', UpdateUniv.as_view(), name='update_univ'),
    path('delete_univ/<slug:slug>/', DeleteUniv.as_view(), name='delete_univ'),
]