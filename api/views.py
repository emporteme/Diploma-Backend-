from .serializers import UniversitySerializer, MajorSerializer, FacultySerializer
from .models import University, Major, Faculty
from .models import NavBar
from .serializers import NavBarSerializer
from rest_framework import generics


class NavBarListCreate(generics.ListCreateAPIView):
    queryset = NavBar.objects.all()
    serializer_class = NavBarSerializer


class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class MajorListCreateView(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class MajorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class FacultyListCreateView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
