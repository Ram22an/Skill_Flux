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
