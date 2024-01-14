from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Musician(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    founding_date = models.DateField()
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.genre}')
        super().save(force_insert, force_update, using, update_fields)
        return f'{self.name} - {self.genre}'

    def get_absolute_url(self):
        return reverse('musician_detail', kwargs={'slug': self.slug})
