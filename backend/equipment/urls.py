from django.urls import path, include
from equipment import views

urlpatterns = [
    path('add/', views.add_equipment),
    path('all/', views.get_all_equipment),
    path('provider/', views.get_providers_equipment),
    path('<int:pk>/update/', views.update_equipment),
]
