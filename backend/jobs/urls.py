from django.urls import path, include
from jobs import views

urlpatterns = [
    path('', views.client_jobs),
    path('all/', views.get_all_jobs),
    path('<int:pk>/update/', views.update_job),
    path('<int:jpk>/services/', views.get_job_services),
    path('<int:jpk>/services/<int:pk>/', views.update_job_services),
]