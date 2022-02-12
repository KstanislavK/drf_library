from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_date = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.birthday_date}'


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)

