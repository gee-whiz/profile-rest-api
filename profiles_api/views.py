from profiles_api import serializers
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test Api View."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'is similar to a traditional django view', 'is ,apped manually to URls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a heloo message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            last_name = serializer.validated_data.get('last_name')
            message = f'Hello {name} {last_name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test API for HelloViewSet."""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve,update, partial_update)',
            'automatically maps to URL using Routers',
            'Provides more functionality with less AuthenticationMiddleware'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            last_name = serializer.validated_data.get('last_name')
            message = f'Hello {name} {last_name}'
            return Response({'MESSAGE':  message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'Http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'Http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'Http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'Http_method': 'DELETE'})
