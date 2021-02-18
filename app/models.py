from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Estate(models.Model):
	estateID = models.IntegerField()
	name = models.CharField(max_length=100)

class Item(models.Model):
	itemID = models.IntegerField()
	name = models.CharField(max_length=100)
	value = models.IntegerField()
	estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)
	status = models.CharField(max_length=100)
	owner_username = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	initial_time = models.DateTimeField(default=timezone.now)
	text = models.TextField()
	updated_time = models.DateTimeField(default=timezone.now)
	itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Wish(models.Model):
	itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	wish = models.CharField(max_length=100)

class Participate(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)