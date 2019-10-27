from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'estimated_duration', 'completed_duration', 'status']
    
    # Check instance status
    def validate(self, data):
        if (self.instance and self.instance.status == 1):
            raise ValidationError('task completed')
        return data