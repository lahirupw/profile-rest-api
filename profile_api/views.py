from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets



class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request,format=None):
        """Return a list of APIview Features"""
        an_apiview =[
            'Uses HTTP method as function (get,post,patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over the application logic',
            'Mapped Manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message  = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request,pk=None):
        """Handle Updating an Object"""
        return Response({'method': 'PUT'})
    def patch(self, request,pk=None):
        """Partial update or field update on an object"""
        return  Response({'method','Patch'})
    def delete(self, request,pk=None):
        """Delete an Object"""
        return Response({'method','DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """Test API viewset"""
    def list(self, request):
        """return a hello message"""
        a_viewset=['Uses actions (List, create, retrive, update, partial update)',
        'Automatically maps to urls using routers',
        'provides more functionality with less code'
        ]
        return Response({'message':'Hellow Viewset','a_viewset':a_viewset})
