from django.urls import path, include
from clients import views

urlpatterns = [
    path('', views.user_clients),
    path('all/', views.get_all_clients),
    path('<int:pk>/update/', views.update_client),
]