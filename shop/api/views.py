from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import BicycleSerializer, CartSerializer
from products.models import Bicycle, Cart


@api_view(['GET'])
def get_bicycles(request):
    bicycles = Bicycle.objects.all()
    serializer = BicycleSerializer(bicycles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)
