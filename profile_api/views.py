from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request,format=None):
        """Return a list of APIview Features"""
        an_apiview =[
            'Uses HTTP method as function (get,post,patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over the application logic',
            'Mapped Manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview': an_apiview})
