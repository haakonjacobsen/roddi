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
    itemID = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    def __str__(self):
        return '%s - %s - %s' % (self.itemID.name, self.name, self.date_added)


class Wish(models.Model):
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = (
        (0 , 'Fordel'),
        (1, 'Doner'),
        (2, 'Kast'),
    )
    choice = models.IntegerField(max_length=1, choices=choices, default=1)

    #share = models.BooleanField(default=False)
    #donate = models.BooleanField(default=False)
    #discard = models.BooleanField(default=False)

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

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estateID = models.ForeignKey(Estate, on_delete=models.CASCADE)

