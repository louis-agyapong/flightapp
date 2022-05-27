from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from flightapp.flight import views

router = DefaultRouter()
router.register("flights", views.FlightViewSet)
router.register("passengers", views.PassengerViewSet)
router.register("reservations", views.ReservationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
