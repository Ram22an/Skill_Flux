from django.db import models
from django.utils.translation import gettext_lazy as _
class AccessRequirement(models.TextChoices):
    ANYONE="any",_("Anyone")
    EMAIL_REQUIRED="email_required",_("Email required")


class PublishStatus(models.TextChoices):
    # "publish" this is what i will see in database
    # "Published" this is what i will see in choices
    PUBLISHED="publish",_("Published")
    COMING_SOON="soon",_("Coming Soon")
    DRAFT="draft",_("Draft")

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    publish_date=models.DateField()
    image=models.ImageField()
    access=models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.ANYONE
    )
    status=models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status==PublishStatus.PUBLISHED
