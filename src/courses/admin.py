from django.contrib import admin
from .models import Course
# Register your models here.
# admin.site.register(Course) or use decorator
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title','publish_date')
    list_filter=('status','access')
    search_fields=('title','description')


