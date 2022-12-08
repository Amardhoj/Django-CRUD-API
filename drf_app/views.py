from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from drf_app.models import Employee
from drf_app.serializers import EmployeeSerializer, LoginSerializer, RegisterSerializer


# API that can perform CRUD operations with the database
class EmployeeAPI(APIView):
    def get(self, request):
        obj = Employee.objects.filter(dept__isnull = False)
        serializer = EmployeeSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Employee.objects.get(id = data['id'])
        serializer = EmployeeSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Employee.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Data Deleted'})


# API that will Register user
class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({'message': 'User created'})


# API that will Login user
class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
        if not user:
            return Response({'message': 'Invalid Credentials'})
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'User Logged in', 'token': str(token)})