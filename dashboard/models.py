from django.db import models

class SalesRep(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Lead(models.Model):
    SERVICE_CHOICES = [
        ('Makeup', 'Makeup'),
        ('Photography', 'Photography'),
        ('Decor', 'Decor'),
    ]
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Scheduled', 'Scheduled'),
        ('Closed', 'Closed'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    event_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    assigned_to = models.ForeignKey(SalesRep, on_delete=models.SET_NULL, null=True, blank=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)

class CallSchedule(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    rep = models.ForeignKey(SalesRep, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Scheduled')  # or Completed/Missed
