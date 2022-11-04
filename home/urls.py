from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('universités/', views.Univs, name='univs'),
    path('université/<str:slug>/', views.UnivSingle, name='univ-single'),
    path('université/<str:slug>/', views.Facs, name='facs'),
    path('faculté/<str:slug>/', views.Deps, name='deps'),
    path('departement/<str:slug>/', views.Proms, name='proms'),
    path('promotion/<str:slug>/', views.PromsInfos, name='prom-infos'),
    path('contact/', views.Contact, name='contact'),
]
