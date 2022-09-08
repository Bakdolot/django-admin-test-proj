from django.contrib.gis.db import models


class WorldBorder(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    area = models.IntegerField(verbose_name="Area")
    pop2005 = models.IntegerField(verbose_name="Population 2005")
    fips = models.CharField(max_length=2, verbose_name="FIPS Code")
    iso2 = models.CharField(max_length=2, verbose_name="2 Digit ISO")
    iso3 = models.CharField(max_length=3, verbose_name="3 Digit ISO")
    un = models.IntegerField(verbose_name="United Nations Code")
    region = models.IntegerField(verbose_name="Region Code")
    subregion = models.IntegerField(verbose_name="Sub-Region Code")
    lon = models.FloatField(verbose_name="Lon")
    lat = models.FloatField(verbose_name="Lat")
    geom = models.MultiPolygonField(srid=4326, verbose_name="Mpoly")
