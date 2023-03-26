from django.db import models
from django.utils.timezone import now
from django.conf import settings
import uuid

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Ordinary Car')
    description = models.CharField(null=False, max_length=200, default='left over')

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CarMake_model = models.ForeignKey(CarMake, on_delete=models.CASCADE,null=True)
    name = models.CharField(null=False, max_length=30, default='Ordinary Car')
    dealer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Sedan='Sedan'
    SUV='SUV'
    WAGON='WAGON'
    type = [
        (Sedan, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    year = models.DateField(null=True)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership,name,purchase,review,purchase_date,car_make,car_model,car_year,sentiment,id):
        # Dealership
        self.dealership = dealership
        # Review name
        self.name = name
        # Dealer purchase
        self.purchase= purchase
        # Dealer review
        self.review= review
        # Dealer purchase
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.sentiment=sentiment
        self.id=id
    def __str__(self):
        return "Dealer review: " + self.review