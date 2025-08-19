from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from .models import Course
# Register your models here.
# admin.site.register(Course) or use decorator
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields=['title','description','publish_date','access','status','image','display_image']
    readonly_fields=['display_image']
    list_display=['title','publish_date','display_image']
    list_filter=['status','access']
    search_fields=['title','description']

    def display_image(self,obj):
        url=obj.image.url
        cloudinary_id=str(obj.image)
        cloudinary_html=CloudinaryImage(cloudinary_id).image(width=100)
        return format_html(cloudinary_html)
    display_image.short_description="Current Image"


