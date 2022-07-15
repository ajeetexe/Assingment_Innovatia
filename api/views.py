from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import RechargeHistroy
from .helpers import airtel_plan, jio_plan, is_price_available, is_number_valid
from .serializers import RechargeSerializers
# Create your views here.


@api_view(['POST'])
def view_plan(request):
    if request.method == 'POST':
        operator_name = request.data.get('operator')
        if operator_name == None:
            return Response(data={"airtel": airtel_plan, "jio": jio_plan}, status=status.HTTP_200_OK)
        elif operator_name.lower() == "airtel":
            return Response(data=airtel_plan, status=status.HTTP_200_OK)
        elif operator_name.lower() == "jio":
            return Response(data=jio_plan, status=status.HTTP_200_OK)

        else:
            return Response(data="Data not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def recharge(request):
    if request.method == 'POST':

        mobile = request.data.get("mobile")
        price = request.data.get("price")
        operator = request.data.get("operator")
        if mobile == None or price == None or operator == None:
            return Response(data="Not found", status=status.HTTP_404_NOT_FOUND)
        if operator.lower() == "airtel":
            check = is_price_available(airtel_plan, price)
            if not check:
                return Response(data="That pack is not availble", status=status.HTTP_404_NOT_FOUND)
        if operator.lower() == "jio":
            check = is_price_available(jio_plan, price)
            if not check:
                return Response(data="That pack is not availble", status=status.HTTP_404_NOT_FOUND)
        if not is_number_valid(mobile):
            return Response(data="Mobile number is not correct", status=status.HTTP_403_FORBIDDEN)
        RechargeHistroy.objects.create(
            mobile_number=mobile, price=price, operator_name=operator)
        return Response(data="Recharge Successfully", status=status.HTTP_201_CREATED)


@api_view(['GET'])
def recharge_history(request):
    if request.method == 'GET':
        history = RechargeHistroy.objects.all()
        serializer = RechargeSerializers(history, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
