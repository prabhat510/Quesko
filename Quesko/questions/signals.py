from django.db.models.signals import pre_save
from django.dispatch import receiver

# we r going to use this to create slug based on content of instance
from django.utils.text import slugify

from core.utils import generate_random_string
from questions.models import Question


@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
