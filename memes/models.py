from django.db import models

# Create your models here.
class Meme(models.Model):
	name = models.CharField(max_length=50)
	created_date = models.DateTimeField()
	img_url = models.URLField(max_length=200)
	description = models.TextField()
	upvote_peak = models.IntegerField(default=0)

	def __str__(self):
		return "{} - {}".format(self.title, self.artist)

