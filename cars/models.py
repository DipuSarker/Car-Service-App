from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.

class Car(models.Model):
    state_choices = (
        ('DK', 'Dhaka'),
        ('RP', 'Rangpur'),
        ('RS', 'Rajshahi'),
        ('SY', 'Sylhet'),
        ('DP', 'Dinajpur'),
        ('CG', 'Chittagong'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))


    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Headset', 'Bluetooth Headset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )

    car_title = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=state_choices)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('year'),choices=year_choice )
    condition = models.CharField(max_length=200)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    interior = models.CharField(max_length=200)
    miles = models.IntegerField()
    doors = models.CharField(max_length=200, choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=200)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=200)
    no_of_owners = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.car_title




    