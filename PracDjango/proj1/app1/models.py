from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    # using enums
    CHAI_TYPE_CHOICE = [
        # tuple of key-value pair
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    # ERROR - Cannot use ImageField because Pillow is not installed.
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)