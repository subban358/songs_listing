from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
# Create your models here.

class Artists(models.Model):
	""" Fields for storing Artists Data """
	artist_name = models.CharField(max_length = 50, blank = False)
	dob = models.DateField()
	bio = models.TextField(max_length = 150)

	def __str__(self):
		return self.artist_name

class Songs(models.Model):
	""" Fields for storing song data """
	song_name = models.CharField(max_length = 30, blank = False)
	genre = models.CharField(max_length = 30, blank = False)
	artist = models.ManyToManyField(Artists)
	cover = models.ImageField(upload_to = 'pics', blank = False)
	release_date = models.DateField()

	def __str__(self):
		return self.song_name

class Ratings(models.Model):
	""" Fields to store all the rating """
	rating = models.IntegerField(default = 0, validators=[MaxValueValidator(5), MinValueValidator(1)])
	song = models.ForeignKey(Songs, on_delete = models.CASCADE)
