from django.db import models
from django.urls import reverse
from datetime import date, timedelta
# Create your models here.

class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.species
    
    def was_fed_recently(self):
        recent_date = date.today() - timedelta(days=1)  # Define your criteria for 'recent'
        return self.feeding_set.filter(date__gte=recent_date).count() > 0

    def feeding_status(self):
        if self.was_fed_recently():
            return 'Fed'
        else:
            return 'Hungry'
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=100)

    # Create a ForeignKey to Finch
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meal} on {self.date}"

    # Redirects to the Finch detail page after adding a feeding
    def get_absolute_url(self):
        return reverse('finch_detail', kwargs={'pk': self.finch.id})