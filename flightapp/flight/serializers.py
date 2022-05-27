from rest_framework import serializers

from .models import Flight, Passenger, Reservation


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


class FlightSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operating_airline",
            "departure_city",
            "arrival_city",
            "departure_time",
            "arrival_time",
            "price",
            "capacity",
            "available_seats",
            "reservations",
        )


class PassengerSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)
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
            "reservations",
        )
