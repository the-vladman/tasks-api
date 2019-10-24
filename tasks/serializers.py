from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'duration', 'recorded_time', 'status']
    
    def validate(self, data):
        if self.instance.status == 1:
            raise ValidationError('task completed')
        return data