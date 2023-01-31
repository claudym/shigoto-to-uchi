from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Item
from api.serializers import ItemSerializer

# ItemList
@api_view(['GET', 'POST'])
def itemList(request, format=None):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Item
@api_view(['GET', 'PUT', 'DELETE'])
def itemDetail(request, pk, format=None):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
