from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, max_length=255, unique=True, default='')
    content = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.title}'
