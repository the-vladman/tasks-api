from django.db import models


PENDING = 0
COMPLETED = 1

TASK_STATUS = (
    (PENDING, 'pending'),
    (COMPLETED, 'completed'),
)

class Task(models.Model):
    description = models.CharField(max_length=250)
    duration = models.PositiveSmallIntegerField()
    recorded_time = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUS, default=0)