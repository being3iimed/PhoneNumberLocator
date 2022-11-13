import phonenumbers
import opencage
import folium

from myphone import MyPhoneNumber

# modules we have to import that we are going to use

# to extract the country name
from phonenumbers import geocoder

# to extract the carrier or service provider
from phonenumbers import carrier

from opencage.geocoder import OpenCageGeocode

# this variable will be containing our number
# (that variable have phone number and basic details)
Pnumber = phonenumbers.parse(MyPhoneNumber)

# getting the region/country
Region = geocoder.description_for_number(Pnumber, "fr")

# Getting carrier/service provider of a phone number
Carrier = carrier.name_for_number(Pnumber, 'fr')


key = 'a407b532323949ed8cdb082e2c2f9393'
geocoder = OpenCageGeocode(key)
query = str(Region)

# return JSON file contain geo infos
res = geocoder.geocode(query)
# getting latitude & longitude from result of the geocoding of "query"
lat = res[0]['geometry']['lat']
lng = res[0]['geometry']['lng']

# creating a variable (map) that we fill the location with our  lat & lng
MMap = folium.Map(Region=[lat, lng], zoom_start=20)

tooltip = "this is the phone location you looking for!"
# marking the phone number location
folium.Marker([lat, lng], popup=Region, tooltip=tooltip).add_to(MMap)

MMap.save("myLocation.html")
