from rest_framework import serializers

from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operating_airline",
            "departure_city",
            "arrival_city",
            "departure_time",
            "arrival_time",
            "price",
            "capacity",
            "available_seats",
        )


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "city",
            "state",
            "zip_code",
            "country",
            "passport_number",
            "passport_expiration_date",
        )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "flight",
            "passenger",
            "seat_number",
            "seat_type",
            "price",
        )
