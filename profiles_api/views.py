from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test Api View."""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete)',
            'is similar to a traditional django view', 'is ,apped manually to URls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
