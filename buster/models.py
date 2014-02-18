from __future__ import unicode_literals

from django.db import models


class BusStop(models.Model):
    id = models.IntegerField(primary_key=True)
    on_street = models.CharField(max_length=200, blank=True)
    cross_street = models.CharField(max_length=200, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_stop'


class BusStopDemographics(models.Model):
    id = models.IntegerField(primary_key=True)
    bus_stop = models.ForeignKey(BusStop, db_column='bus_stop', blank=True, null=True)
    pct_income_below_poverty = models.FloatField(blank=True, null=True)
    pct_income_less_than_25 = models.FloatField(blank=True, null=True)
    pct_income_between_25_and_50 = models.FloatField(blank=True, null=True)
    pct_income_between_50_and_100 = models.FloatField(blank=True, null=True)
    pct_income_between_100_and_200 = models.FloatField(blank=True, null=True)
    pct_income_greater_than_200 = models.FloatField(blank=True, null=True)
    median_income = models.FloatField(blank=True, null=True)
    pct_highschool_graduate = models.FloatField(blank=True, null=True)
    pct_bachelors_degree_or_higher = models.FloatField(blank=True, null=True)
    population_density = models.FloatField(blank=True, null=True)
    us_population_eighteen_to_twenty_four_years_old = models.FloatField(blank=True, null=True)
    us_population_under_one_year_old = models.FloatField(blank=True, null=True)
    us_population_one_to_four_years_olds = models.FloatField(blank=True, null=True)
    us_population_twenty_five_to_sixty_four_years_old = models.FloatField(blank=True, null=True)
    us_population_five_to_seventeen_years_old = models.FloatField(blank=True, null=True)
    us_population_over_seventy_nine_years_old = models.FloatField(blank=True, null=True)
    us_population_sixty_five_to_seventy_nine_years_old = models.FloatField(blank=True, null=True)
    us_housing_units = models.FloatField(blank=True, null=True)
    us_housing_units_owner_occupied = models.FloatField(blank=True, null=True)
    us_housing_units_no_vehicle = models.FloatField(blank=True, null=True)
    us_housing_units_occupied = models.FloatField(blank=True, null=True)
    us_housing_units_one_person = models.FloatField(blank=True, null=True)
    us_housing_units_1970_to_1989 = models.FloatField(blank=True, null=True)
    us_housing_units_after_1990 = models.FloatField(blank=True, null=True)
    us_housing_units_1950_to_1969 = models.FloatField(blank=True, null=True)
    us_housing_units_before_1950 = models.FloatField(blank=True, null=True)
    us_population_foreign_born = models.FloatField(blank=True, null=True)
    us_population_severe_poverty = models.FloatField(blank=True, null=True)
    us_population_hispanic_or_latino = models.FloatField(blank=True, null=True)
    us_population_white_not_hispanic = models.FloatField(blank=True, null=True)
    us_population_white = models.FloatField(blank=True, null=True)
    us_population_native_hawaiian_and_other_pacific_islander = models.FloatField(blank=True, null=True)
    us_population_asian = models.FloatField(blank=True, null=True)
    us_population_black_or_african_american = models.FloatField(blank=True, null=True)
    us_population_low_income = models.FloatField(blank=True, null=True)
    us_population_poverty = models.FloatField(blank=True, null=True)
    us_population = models.FloatField(blank=True, null=True)
    us_households = models.FloatField(blank=True, null=True)
    us_households_single_mothers = models.FloatField(blank=True, null=True)
    us_housing_units_vacation = models.FloatField(blank=True, null=True)
    us_population_black_or_african_american_not_hispanic = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_stop_demographics'


class BusStopRidership(models.Model):
    id = models.IntegerField(primary_key=True)
    bus_stop = models.ForeignKey(BusStop, db_column='bus_stop', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    day_type = models.CharField(max_length=20, blank=True)
    boardings = models.FloatField(blank=True, null=True)
    alightings = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_stop_ridership'


class ChicagoWeather(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    precipitation = models.FloatField(blank=True, null=True)
    cloud_cover = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chicago_weather'


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    route = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'route'


class RouteRidership(models.Model):
    id = models.IntegerField(primary_key=True)
    bus_route = models.ForeignKey(Route, db_column='bus_route', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    day_type = models.CharField(max_length=20, blank=True)
    rides = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_ridership'


class RoutesAndStops(models.Model):
    stop = models.ForeignKey(BusStop)
    route = models.ForeignKey(Route)

    class Meta:
        managed = False
        db_table = 'routes_and_stops'
