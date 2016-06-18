from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=150)
	create_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(blank=True, null=True)
	content = models.TextField()

	def Publish(self):
		self.pub_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
