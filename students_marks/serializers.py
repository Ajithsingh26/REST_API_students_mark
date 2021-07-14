from rest_framework import serializers
from .models import students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'