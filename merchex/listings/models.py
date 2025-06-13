from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50,default='Rock')
    biography = models.fields.CharField(max_length=1000,default='No biography available')
    year_formed = models.fields.IntegerField( validators=[MinValueValidator(1900), MaxValueValidator(2021)], null=True)
    active = models.fields.BooleanField(default=True,null=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


    def __str__(self):
        return self.name
    
class Listing(models.Model):
    liste=(
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
        ('Cassette', 'Cassette'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)],null=True)
    type = models.CharField(max_length=10, choices=liste)
    band=models.ForeignKey(Band,on_delete=models.CASCADE, related_name='listings', null=True, blank=True)

    def __str__(self):
        return self.title;
