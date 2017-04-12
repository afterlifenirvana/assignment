from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import permissions
from operator import itemgetter
import json


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def restaurant_list(request):
    """
    List all restaurants, or create a new Restaurant.
    """
    if request.method == 'GET':
        restaurants = Restaurants.objects[:10]
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def restaurant_detail(request, pk):
    """
    Retrieve, update or delete a Restaurant instance.
    """
    try:
        restaurants = Restaurants.objects.get(pk=pk)
    except Restaurants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurants)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurants, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@permission_classes((permissions.AllowAny,))
def test(request):
    if request.method == 'GET':
        cuisine_data = Restaurants.objects.item_frequencies('cuisine')
        serializer = RestaurantSerializer(cuisine_data,many=True)
        pipe = [ { "$unwind": "$grades" },
         { "$group" : { "_id": {"name":"$name","borough":"$borough","cuisine":"$cuisine"},
         "avgGrade": { "$avg" : "$grades.score" }} },
          {"$sort": {"avgGrade": -1}}, { "$limit": 10}, ]
        top = Restaurants._get_collection().aggregate(pipeline=pipe)
        # cuisine_data = sorted(cuisine_data.items(),key=itemgetter(1),reverse=True)
        # return
        # Response({'cuisine':cuisine_data,'top':top['result']},template_name='templates/api/index.html')
        return Response({'cuisine': json.dumps(cuisine_data),'top':top['result']}, template_name='templates/api/index.html')
