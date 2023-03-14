from django.urls import path
from . import views

urlpatterns = [
    path('api/navbar/', views.NavBarListCreate.as_view()),
    path('api/universities/', views.UniversityListCreateView.as_view()),
    path('api/universities/<int:pk>/', views.UniversityDetailView.as_view()),
    path('api/majors/', views.MajorListCreateView.as_view()),
    path('api/majors/<int:pk>/', views.MajorDetailView.as_view()),
    path('api/faculties/', views.FacultyListCreateView.as_view()),
    path('api/faculties/<int:pk>/', views.FacultyDetailView.as_view()),
]
