from django.db import models
from django.utils.translation import gettext_lazy as _


class Flight(models.Model):
    flight_number = models.CharField(_("Flight Number"), max_length=256)
    operating_airline = models.CharField(_("Operating Airline"), max_length=256)
    departure_city = models.CharField(_("Departure City"), max_length=256)
    arrival_city = models.CharField(_("Arrival City"), max_length=256)
    departure_time = models.DateTimeField(_("Departure Time"))
    arrival_time = models.DateTimeField(_("Arrival Time"))
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    capacity = models.IntegerField(_("Capacity"))
    available_seats = models.IntegerField(_("Available Seats"))

    def find_available_seats(self):
        return self.capacity - Reservation.objects.filter(flight=self).count()

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    first_name = models.CharField(_("First Name"), max_length=256)
    last_name = models.CharField(_("Last Name"), max_length=256)
    email = models.EmailField(_("Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=256)
    address = models.CharField(_("Address"), max_length=256)
    city = models.CharField(_("City"), max_length=256)
    state = models.CharField(_("State"), max_length=256)
    zip_code = models.CharField(_("Zip Code"), max_length=256)
    country = models.CharField(_("Country"), max_length=256)
    passport_number = models.CharField(_("Passport Number"), max_length=256)
    passport_expiration_date = models.DateField(_("Passport Expiration Date"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name="reservations")
    seat_number = models.CharField(_("Seat Number"), max_length=256)
    seat_type = models.CharField(_("Seat Type"), max_length=256)
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.flight} - {self.passenger}"
