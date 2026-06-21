from django.db import models

class TourPackage(models.Model):
    PACKAGE_TYPES = [
        ('cultural', 'Cultural & Historical'),
        ('adventure', 'Adventure & Nature'),
        ('extreme', 'Extreme Adventure'),
    ]
    
    name = models.CharField(max_length=200)
    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPES)
    location = models.CharField(max_length=200)
    price = models.IntegerField(help_text="Price in ETB")
    duration_days = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    number_of_people = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.package.name}"