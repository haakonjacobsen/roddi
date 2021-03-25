from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Estate(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)
    description = models.TextField(default="Beskrivelse mangler")


class Comment(models.Model):
    itemID = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    def __str__(self):
        return '%s - %s - %s' % (self.itemID.name, self.name, self.date_added)


class Wish(models.Model):
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.BooleanField(default=False)
    donate = models.BooleanField(default=False)
    discard = models.BooleanField(default=False)


class Participate(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)
