import json

import requests
from bs4 import BeautifulSoup  # type: ignore

url = "https://www.immoweb.be/fr/annonce/maison-de-maitre\
    /a-vendre/antwerpen/2600/9347744"


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    url_data = str(soup.select("#container-main-content div script")[0])
    url_data = (
        url_data.replace("</script>", "")
        .replace('<script type="text/javascript">', "")
        .replace("window.classified = ", "")
        .replace(" ", "")
        .replace(";", "")
    )

    json_data = json.loads(url_data)

    print("locality: " + str(json_data["property"]["location"]["postalCode"]))
    print("Tpe of property: " + str(json_data["property"]["type"]))
    print("Subtype of property: " + str(json_data["property"]["subtype"]))
    print("price: " + str(json_data["transaction"]["sale"]["price"]))
    print("Type of sale: " + str(json_data["price"]["type"]))
    print("Number of rooms: " + str(json_data["property"]["bedroomCount"]))
    print("Area: " + str(json_data["property"]["netHabitableSurface"]))
    print(
        "Fully equipped kitchen: "
        + str(json_data["property"]["kitchen"]["type"])
    )
    print("Furnished: " + str(json_data["transaction"]["sale"]["isFurnished"]))
    print("Open fire: " + str(json_data["property"]["fireplaceExists"]))
    print("Terrace" + str(json_data["property"]["hasTerrace"]))
    print("Garden : " + str(json_data["property"]["hasGarden"]))
    print(
        "Surface of the land: " + str(json_data["property"]["land"]["surface"])
    )
    print(
        "Number of facades: "
        + str(json_data["property"]["building"]["facadeCount"])
    )
    print("Swimming pool: " + str(json_data["property"]["hasSwimmingPool"]))
    print(
        "State of the building: "
        + str(json_data["property"]["building"]["condition"])
    )
