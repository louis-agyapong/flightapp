from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


def find_flights(request):
    return Flight.objects.filter(
        departure_city=request.data["departure_city"],
        arrival_city=request.data["arrival_city"],
        departure_time=request.data["departure_time"],
    )


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
