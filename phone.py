import phonenumbers
import opencage
import urllib3
from folium import folium
from test import number

from phonenumbers import geocoder ### Building function for phonenumbers:
pepnumber = phonenumbers.parse(number) ### Country History.
location= geocoder.description_for_number(pepnumber,"en")
print(location)


### from another bulding function
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en")) ### en means english language.

from opencage.geocoder import OpenCageGeocode

key ='c2a413ad5be7449a89c391ce6c997bed'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat'] #latitude=lat
lng = results[0]['geometry']['lng'] # longeitude=lng

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup= location).add_to(myMap)

myMap.save("mylocation.html")
