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
    Favorite = models.ManyToManyField(User, default=None, blank=True, related_name='Ønsket')
    

    def __str__(self):
        return str(self.name)


    @property
    def num_favorite(self):
        return self.Favorite.all().count()



class Comment(models.Model):
    initial_time = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    updated_time = models.DateTimeField(default=timezone.now)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Wish(models.Model):
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.BooleanField(default=False)
    donate = models.BooleanField(default=False)
    discard = models.BooleanField(default=False)

WISH_CHOICES = (
    ('Ønsket', 'Ønsket'),
    ('Angre ønsket', 'Angre ønsket'),
)

class Favorite(models.Model):
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.CharField(choices=WISH_CHOICES, default='Ønsket', max_length=50)

    def __str__(self):
        return str(self.itemID)


class Participate(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)
