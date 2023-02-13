from django.urls import path, include
from jobs import views

urlpatterns = [
    path('', views.user_jobs),
    path('all/', views.get_all_jobs),
    path('<int:pk>/update/', views.update_job),
]