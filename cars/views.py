from rest_framework import generics

from cars.models import Car
from cars.serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CarListView(APIView):
#     """
#     List all cars, or create one.
#     """
#     def get(self, request, format=None):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class CarDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404

#     def get(self, requst, pk, format=None):
#         car = self.get_object(pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         car = self.get_object(pk)
#         serializer = CarSerializer(car, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, fotmai=None):
#         car = self.get_object(pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def car_list(request, format=None):
#     """
#     List of all cars, or create a new car.
#     """
#     if request.method == 'GET':
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CarSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def car_detail(request, pk, format=None):
#     """
#     Retrive, update or delete a car.
#     """
#     try:
#         car = Car.objects.get(pk=pk)
#     except Car.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CarSerializer(car)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CarSerializer(car, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
