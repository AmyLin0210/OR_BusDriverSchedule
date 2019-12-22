from django.db import models
import os
# from . import seetings

# file_ = open(os.path.join(settings.BASE_DIR, 'static/route.json'))
# Create your models here.
class Route (models.Model):
    route_name = models.CharField(max_length = 20)

class Route_item (models.Model):
    route_id  = models.ForeignKey(Route, on_delete=models.CASCADE)
    item_id   = models.DecimalField(max_digits = 2, decimal_places=0)
    item_name = models.CharField(max_length=50)
    item_note = models.CharField(max_length=200)

class Route_detail (models.Model):
    route_item_id = models.ForeignKey(Route_item, on_delete=models.CASCADE)
    detail_id = models.DecimalField(max_digits = 3, decimal_places=0)

class Route_stop (models.Model):
    route_item_id = models.ForeignKey(Route_item, on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=15)
    stop_index = models.DecimalField(max_digits = 1, decimal_places=0)

class Route_stop_time (models.Model):
    route_stop_id = models.ForeignKey(Route_stop, on_delete=models.CASCADE)
    route_detail_id = models.ForeignKey(Route_detail, on_delete=models.CASCADE)
    stop_time = models.CharField(max_length=10)

class Schedule_date (models.Model):
    date = models.CharField(max_length=12)

class Schedule_driver (models.Model):
    schedule_id = models.ForeignKey(Schedule_date, on_delete=models.CASCADE)
    driver_id = models.DecimalField(max_digits = 4, decimal_places=0) 
