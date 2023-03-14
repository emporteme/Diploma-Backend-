from django.db import models


class NavBar(models.Model):
    navName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


def default_image():
    return "https://example.com/default-image.jpg"


class University(models.Model):
    unik_title = models.CharField(max_length=255)
    unik_description = models.TextField()
    unik_date_created = models.DateField(auto_now_add=True)
    unik_study_type = models.CharField(max_length=255)
    unik_lang = models.CharField(max_length=255)
    unik_major = models.ForeignKey('Major', on_delete=models.CASCADE)
    unik_img = models.ImageField(
        upload_to='images/', default=default_image, blank=True)
    unik_logo = models.ImageField(
        upload_to='images/', default=default_image, blank=True)
    unik_min_unt = models.DecimalField(max_digits=5, decimal_places=2)
    unik_min_ielts = models.DecimalField(max_digits=4, decimal_places=1)
    unik_student_num = models.PositiveIntegerField()
    unik_study_year_num = models.PositiveIntegerField()
    unik_location = models.CharField(max_length=255)
    unik_website = models.URLField()
    unik_tuition = models.DecimalField(max_digits=7, decimal_places=2)
    unik_admission_criteria = models.TextField()
    unik_faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    unik_student_life = models.TextField()
    unik_campus_housing = models.TextField()

    def __str__(self):
        return self.unik_title


class Major(models.Model):
    major_title = models.CharField(max_length=255)
    major_description = models.TextField()
    major_parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.major_title


class Faculty(models.Model):
    faculty_title = models.CharField(max_length=255)
    faculty_description = models.TextField()

    def __str__(self):
        return self.faculty_title
