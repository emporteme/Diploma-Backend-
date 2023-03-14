from .models import University, Major, Faculty
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import NavBar


@admin.register(NavBar)
class NavBarAdmin(admin.ModelAdmin):
    list_display = ['navName', 'created_at']


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('unik_title', 'unik_study_type',
                    'unik_location', 'unik_faculty', 'unik_major')
    list_filter = ('unik_study_type', 'unik_faculty', 'unik_major')
    search_fields = ('unik_title', 'unik_location')
    fieldsets = (
        ('University Details', {
            'fields': ('unik_title', 'unik_description', 'unik_study_type', 'unik_lang', 'unik_major', 'unik_faculty')
        }),
        ('University Images', {
            'fields': ('unik_img', 'unik_logo')
        }),
        ('University Requirements', {
            'fields': ('unik_min_unt', 'unik_min_ielts', 'unik_tuition', 'unik_admission_criteria')
        }),
        ('University Information', {
            'fields': ('unik_student_num', 'unik_study_year_num', 'unik_location', 'unik_website', 'unik_student_life', 'unik_campus_housing')
        }),
    )
    readonly_fields = ('unik_date_created',)


class MajorAdmin(admin.ModelAdmin):
    list_display = ('major_title', 'major_parent')
    list_filter = ('major_parent',)
    search_fields = ('major_title', 'major_parent')


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_title',)
    search_fields = ('faculty_title',)


admin.site.register(University, UniversityAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Faculty, FacultyAdmin)
