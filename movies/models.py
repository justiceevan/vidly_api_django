from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    numberInStock = models.IntegerField(default=0, blank=True, null=True)
    dailyRentalRate = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title
