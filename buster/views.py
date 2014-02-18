from django.shortcuts import render
from models import BusStop, BusStopRidership, BusStopDemographics
from dajaxice.decorators import dajaxice_register


# Create your views here.
def home(request):
    """
    Sends the visitor to the homepage, populates data in the map.

    :param request: http request object
    :return:
    """
    bus_stop = BusStop.objects.select_related('busstopridership', 'busstopdemographics', 'routesandstops').all()

    bus_stop_data = []

    for b in bus_stop:
        bus_stop_data.append(dict(
            stop=b.id,
            streets=str(b.on_street) + ' and ' + str(b.cross_street),
            latitude=b.latitude,
            longitude=b.longitude,
            boardings=b.busstopridership.boardings,
            alightings=b.busstopridership.alightings,
            median_income=b.busstopdemographics.median_income,
        ))

    return render(request, template_name='index.html', dictionary=dict(bus_stop_data=bus_stop_data))