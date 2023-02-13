from django.urls import path, include
from services import views

urlpatterns = [
    path('', views.user_services),
    path('all/', views.get_all_services),
    path('all/', views.get_providers_services),
    path('<int:pk>/update/', views.update_service),
]
