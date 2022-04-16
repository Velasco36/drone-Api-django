from enum import _auto_null, auto
from unicodedata import name
from django.db import models
from requests import ReadTimeout


class DroneCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(
        DroneCategory,
        related_name = 'drones',
        on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_copeted = models.BooleanField(default=False)
    

    class Meta:
        ordering = ('name',)

    def __str__(self) :
        return self.name

class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    rances_count = models.IntegerField()
   


    class Meta:
        ordering = ('name',)

    def __str__(self) :
        return self.name


class Copetition(models.Model):
    pilot = models.ForeignKey(
        Pilot,
        related_name='competitions',
        on_delete=models.CASCADE)
    drone = models.ForeignKey(
        Drone,
        on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        # Orden by distance in descending order
        ordering = ('-distance_in_feet',)



