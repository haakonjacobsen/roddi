from django.db import models

class Item(models.Model):
	title = models.CharFiel(max_lenght=100)
	content = models.TextField()