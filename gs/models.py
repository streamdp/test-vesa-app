from django.db import models


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def create_fan(self, pic_url, num, type, diameter, airflow, airflow_unit, pressure, pressure_unit, efficiently):
        fan = self.model(pic_url=pic_url, num=num, type=type, diameter=diameter, airflow=airflow,
                         airflow_unit=airflow_unit, pressure=pressure, pressure_unit=pressure_unit,
                         efficiently=efficiently)
        fan.save()


class Fan(models.Model):
    M3S = 'M3S'
    AIRFLOW_UNIT_CHOICES = [
        ('M3S', 'm³/s'),
        ('M3H', 'm³/h'),
        ('CFM', 'CFM'),
    ]

    PA = 'PA'
    PRESSURE_UNIT_CHOICES = [
        ('PA', 'Pa'),
        ('WC', 'WC'),
    ]

    pic_url = models.CharField(max_length=255)
    num = models.IntegerField(default=0)
    type = models.CharField(max_length=255)
    diameter = models.IntegerField(default=0)
    airflow = models.IntegerField(default=0)
    airflow_unit = models.CharField(max_length=3, choices=AIRFLOW_UNIT_CHOICES, default=M3S)
    pressure = models.FloatField(default=0)
    pressure_unit = models.CharField(max_length=2, choices=PRESSURE_UNIT_CHOICES, default=PA)
    efficiently = models.FloatField(default=0)
    objects = QuestionManager()
