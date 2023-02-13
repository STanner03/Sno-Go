from django.urls import path, include
from providers import views

urlpatterns = [
    path('', views.user_providers),
    path('all/', views.get_all_providers),
    path('<int:pk>/update/', views.update_provider),
    path('<int:ppk>/equipment/', include('equipment.urls')),
    path('<int:ppk>/service/', include('services.urls')),
]