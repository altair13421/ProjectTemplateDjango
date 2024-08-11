from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


# Custom permission class
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # Add your custom permission logic here
        return True


# Example usage of built-in permissions
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Add your code logic here
        return Response("GET request")

    def post(self, request):
        # Add your code logic here
        return Response("POST request")


# Example usage of custom permission
class CustomView(APIView):
    permission_classes = [CustomPermission]

    def get(self, request):
        # Add your code logic here
        return Response("GET request")

    def post(self, request):
        # Add your code logic here
        return Response("POST request")
