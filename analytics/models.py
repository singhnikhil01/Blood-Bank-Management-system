from django.db import models
class BloodDemandData(models.Model):
    bloodgroup = models.CharField(max_length=10)
    date = models.DateField()
    requests = models.PositiveIntegerField(default=0)
    donations = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.bloodgroup} - {self.date}"
