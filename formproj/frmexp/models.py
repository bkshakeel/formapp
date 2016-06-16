from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Article)
def abcde(sender, **kwargs):
    if kwargs.get('created',False):
        a=True
        print ("is a signal sent",a)
