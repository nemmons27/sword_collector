from django.db import models
from django.urls import reverse

JOBS = (
    ('P','Polish')
    ('S','Sharpen')
    ('R','Remodel')
)

# Create your models here.
class Sword(models.Model):
    name = models.CharField(max_length=100)
    legend = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    firstSeen = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sword_id': self.id})

class Swordsmith(models.Model):
    date = models.DateField()
    job = models.CharField(
        max_length=1,
        choices=JOBS,
        default=JOBS[0][0]
        )
    sword = models.ForeignKey(Sword, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_job_display()} on {self.date}"