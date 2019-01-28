from django.db import models
from django.utils.text import slugify

class MenuManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('parent')
        
class Menu(models.Model):
    text = models.CharField(max_length=100, default=None, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, 
                               null=True, default=None, related_name='subs')
    url = models.SlugField(max_length=200, unique=True, blank=True)
    objects = models.Manager()
    menu_manager = MenuManager()

    def __repr__(self):
        return self.text
    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.url = slugify(self.text)
        super(Menu, self).save(*args, **kwargs)