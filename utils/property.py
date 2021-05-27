import json

import requests
from bs4 import BeautifulSoup  # type: ignore


class Property:
    def __init__(self, url) -> None:
        """Property constructor"""
        self.url = url

    def get_data(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "lxml")
        url_data = str(
            soup.select_one("#container-main-content div  script").string
        )
        url_data = (
            url_data.replace("window.classified = ", "")
            .replace(" ", "")
            .replace(";", "")
        )

        json_data = json.loads(url_data)

        self.locality = json_data["property"]["location"]["postalCode"]
        self.property_type = json_data["property"]["type"]
        self.property_subtype = json_data["property"]["subtype"]
        self.price = json_data["transaction"]["sale"]["price"]
        self.sale_type = json_data["price"]["type"]
        self.rooms = json_data["property"]["bedroomCount"]
        self.area = json_data["property"]["netHabitableSurface"]
        self.is_kitchen_equipped = json_data["property"]["kitchen"]["type"]
        self.is_furnished = json_data["transaction"]["sale"]["isFurnished"]
        self.has_open_fire = json_data["property"]["fireplaceExists"]
        self.has_terrace = json_data["property"]["hasTerrace"]
        self.terrace_surface = json_data["property"]["terraceSurface"]
        self.has_garden = json_data["property"]["hasGarden"]
        self.garden_surface = json_data["property"]["gardenSurface"]
        self.land_surface = json_data["property"]["land"]["surface"]
        self.facade_number = json_data["property"]["building"]["facadeCount"]
        self.has_swimming_pool = json_data["property"]["hasSwimmingPool"]
        self.property_state = json_data["property"]["building"]["condition"]
