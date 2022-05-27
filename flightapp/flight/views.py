from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


@api_view(["POST"])
def find_flights(request):
    flights = Flight.objects.filter(
        departure_city=request.data["departure_city"],
        arrival_city=request.data["arrival_city"],
        departure_time=request.data["departure_time"],
    )
    serializer_class = FlightSerializer(flights, many=True)
    return Response(serializer_class.data)

@api_view(["POST"])
def save_reservation(request):
    flight = get_object_or_404(Flight, pk=request.data["id"])
    passenger = Passenger(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        email=request.data["email"],
        phone_number=request.data["phone_number"],
        address=request.data["address"],
        city=request.data["city"],
        state=request.data["state"],
        zip_code=request.data["zip_code"],
        country=request.data["country"],
        passport_number=request.data["passport_number"],
        passport_expiration_date=request.data["passport_expiration_date"],
    )
    passenger.save()
    reservation = Reservation(
        flight=flight,
        passenger=passenger,
        seat_number=request.data["seat_number"],
        seat_type=request.data["seat_type"],
        price=request.data["price"],
    )
    reservation.save()
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data, status=HTTPStatus.CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
