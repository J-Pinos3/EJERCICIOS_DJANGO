from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Task
        #fields = ('id', 'title', 'description', 'done', )
        #si tuviera muchos campos en el model, puedo resumirlo así
        fields = '__all__'