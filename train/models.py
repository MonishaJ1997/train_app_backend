from django.db import models

# Create your models here.

# models.py
from django.db import models

class SiteLogo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    





# models.py
from django.db import models

class TrainBanner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='train_banner/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


    from django.db import models

class TrainMap(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='train_map/')

    def __str__(self):
        return self.title

from django.db import models

class Train(models.Model):
    train_number = models.CharField(max_length=20)
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.TimeField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.train_number} - {self.source} to {self.destination}"





class TrainSchedule(models.Model):
    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE,
        related_name="schedules"
    )
    station_code = models.CharField(max_length=10)
    station_name = models.CharField(max_length=100)
    route_number = models.IntegerField()
    arrival_time = models.TimeField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    halt_minutes = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField()
    day_number = models.IntegerField()
    class Meta:
        ordering = ["route_number"]

    def __str__(self):
        return f"{self.train.train_number} - {self.station_name}"












class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner {self.id}"



from django.db import models

class TravelPackage(models.Model):
    CATEGORY_CHOICES = [
        ('luxury_train', 'Luxury Train'),
        ('international', 'International'),
        ('domestic_air', 'Domestic Air'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='packages/')
    short_description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    




    from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="stations/", blank=True, null=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hours = models.CharField(max_length=100, default="Open - 24 Hours")

    def __str__(self):
        return f"{self.name} ({self.code})"





        
from django.db import models

class TourBanner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tour_banner/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



        # tour/models.py
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title