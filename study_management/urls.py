from django.urls import path
from studies import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_study, name='add_study'),
    path('view/<int:pk>/', views.view_study, name='view_study'),
    path('edit/<int:pk>/', views.edit_study, name='edit_study'),
    path('delete/', views.delete_study, name='delete_study'),
]
