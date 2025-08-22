from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
import helpers
helpers.cloudinary_init()

class AccessRequirement(models.TextChoices):
    ANYONE="any",_("Anyone")
    EMAIL_REQUIRED="email_required",_("Email required")


class PublishStatus(models.TextChoices):
    # "publish" this is what i will see in database
    # "Published" this is what i will see in choices
    PUBLISHED="publish",_("Published")
    COMING_SOON="soon",_("Coming Soon")
    DRAFT="draft",_("Draft")

def handle_upload(instance,filename):
    return f"{filename}"


# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    publish_date=models.DateField()
    # image=models.ImageField(upload_to=handle_upload,blank=True,null=True)
    image=CloudinaryField("image",null=True)
    access=models.CharField(
        max_length=20,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status=models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status==PublishStatus.PUBLISHED
    
    @property
    def image_admin(self):
        if not self.image:
            return ""
        image_options={
            "width":200
        }
        url=self.image.build_url(**image_options)
        return url
    
    def get_image_thumbnail(self,as_html=False,width=500):
        if not self.image:
            return ""
        image_options={
            "width":width
        }
        if as_html:
            # format_html(f"<img src='{url}'/>") = manual <img> tag.
            # self.image.image(...) = Cloudinary-powered <img> tag with transformations baked in.
            return self.image.image(**image_options) 
        
        # self.image.url = plain, original Cloudinary URL.
        # self.image.build_url(...) = smart, customizable URL builder.
        url=self.image.build_url(**image_options)
        return url

# Lesson.objects.all() # lesson queryset -> all rows
# Lesson.objects.first() # lesson queryset -> first rows
# course_obj=Course.objects.first()
# Lesson.objects.filter(course__id=course_obj.id)

# course_obj.Lesson__set.all()

# lessonObj=lesson.objects.all()
# courseobj=lessonObj.course
# ne_course_lesson=courseobj.lesson__set.all()

class Lesson(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    thumbnail=CloudinaryField("image",blank=True,null=True)
    video=CloudinaryField("video",blank=True,null=True,resource_type='video')
    can_preview=models.BooleanField(default=False,help_text="if user does not have access to course, can they see this?")
    status=models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )



