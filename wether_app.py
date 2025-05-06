import requests
import json
import pprint

accuWetherAPIKey = 'JS3Co727CmgUg8qVhexHuan0V2GA0LHm'
r=requests.get("http://www.geoplugin.net/json.gp")

if  r.status_code != 200:
    print("Não foi possivel obter a localização")

else:
    localizacao = json.loads(r.text)

    latitude = localizacao['geoplugin_latitude']
    longitude = localizacao['geoplugin_longitude']
    locationURL = "http://dataservice.accuweather.com/locations/v1/cities"\
    + "/geoposition/search?apikey="+accuWetherAPIKey+"&q="+latitude+"%2C%20"+longitude+"&language=pt-br"

    r2 = requests.get(locationURL)
    if  r.status_code != 200:
        print("Não foi possivel obter o codigo do local")

    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ", " \
        + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
        + locationResponse['Country']['LocalizedName'] 

        codigoLocal = locationResponse['Key']

        print("Local: ", nomeLocal)
        print("Codigo: ", codigoLocal)


   
