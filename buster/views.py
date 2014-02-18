from django.shortcuts import render
from models import BusStopRidership


# Create your views here.
def home(request):
    """
    Sends the visitor to the homepage, populates data in the map.

    :param request: http request object
    :return:
    """
    bus_stops = BusStopRidership.objects.all()

    bus_stop_data = [dict(
        stop=b_s.bus_stop.id,
        streets=str(b_s.bus_stop.on_street) + ' and ' + str(b_s.bus_stop.cross_street),
        latitude=b_s.bus_stop.latitude,
        longitude=b_s.bus_stop.longitude,
        boardings=b_s.boardings,
        alightings=b_s.alightings,
    ) for b_s in bus_stops]

    return render(request, template_name='index.html', dictionary=dict(bus_stop_data=bus_stop_data))