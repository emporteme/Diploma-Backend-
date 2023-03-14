from .models import University, Major, Faculty
from rest_framework import serializers
from .models import NavBar


class NavBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBar
        fields = ('id', 'navName')


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = (
            'id', 'unik_title', 'unik_description', 'unik_date_created',
            'unik_study_type', 'unik_lang', 'unik_major', 'unik_img', 'unik_logo',
            'unik_min_unt', 'unik_min_ielts', 'unik_student_num',
            'unik_study_year_num', 'unik_location', 'unik_website',
            'unik_tuition', 'unik_admission_criteria', 'unik_faculty',
            'unik_student_life', 'unik_campus_housing'
        )


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('id', 'major_title', 'major_description', 'major_parent')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'faculty_title', 'faculty_description')
