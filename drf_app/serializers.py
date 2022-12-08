from rest_framework import serializers
from .models import Employee, Department
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_name', 'location']


class EmployeeSerializer(serializers.ModelSerializer):
    dept = DepartmentSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'
        #depth = 1

    def validate(self, data):
        special_characters = "!@#$%^&*()-=_+/<>?{}[]\|"
        if any(x in special_characters for x in data['name']):
            raise serializers.ValidationError('Name cannot contain special characters')

        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        return data

    
    
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Username is already taken')

        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('Email is already in use')
        
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


        