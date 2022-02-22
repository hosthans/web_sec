from time import timezone
import datetime
from django.db import models


class PC_DATA(models.Model):
    packages_l_h = models.IntegerField()
    update_time_p_l_h = models.DateTimeField('date published')

    def __str__(self):
        return "Packagecount: " + self.packages_l_h.__str__()

    def was_updated_recently(self):
        return self.update_time_p_l_h >= timezone.now() - datetime.timedelta(days=1)