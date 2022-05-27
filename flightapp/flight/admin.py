from django.contrib import admin
from .models import Flight, Passenger, Reservation


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        "flight_number",
        "operating_airline",
        "departure_city",
        "arrival_city",
        "departure_time",
        "arrival_time",
        "price",
        "capacity",
        "available_seats",
    ]
    list_display_links = ["flight_number"]
    list_filter = ["departure_city", "arrival_city"]
    search_fields = ["flight_number", "operating_airline", "departure_city", "arrival_city"]


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = [
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
    ]
    list_display_links = ["first_name", "last_name"]
    list_filter = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["flight", "passenger", "seat_number", "seat_type", "price"]
    list_display_links = ["flight", "passenger"]
    list_filter = ["flight", "passenger"]
    search_fields = ["flight", "passenger"]
