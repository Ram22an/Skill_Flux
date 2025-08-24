from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from .models import Course,Lesson

class LessonInLine(admin.StackedInline):
    model=Lesson
    readonly_fields=['update']
    extra=0



# Register your models here.
# admin.site.register(Course) or use decorator
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=[LessonInLine]
    fields=['title','description','timestamp','access','status','image','display_image','updated']
    readonly_fields=['display_image','timestamp','updated']
    list_display=['title','timestamp','display_image']
    list_filter=['status','access']
    search_fields=['title','description']

    def display_image(self,obj):
        # url=obj.image.url
        url=obj.image_admin
        # cloudinary_id=str(obj.image)
        # cloudinary_html=CloudinaryImage(cloudinary_id).image(width=100)
        return format_html(f"<img src={url}/img>")
    display_image.short_description="Current Image"


