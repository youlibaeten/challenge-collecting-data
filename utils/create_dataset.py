""""

Project name : challenge-collecting-data

Date of last revision: 25/05/2021

Autor(s) : Vincent Kervyn de Meerendré

Revision N° : Version 1

Client : Becode Bouman3.31

Learning objectives :
_____________________
   Use a python library to collect as much data as possible.

At the end of this challenge, you should:

Be able to scrape a website.
Be able to build a dataset from scratch.
Be able to Implement a strategy to collect as much data as possible as a group.
Be able to work as group.

The Mission:
___________
The real estate company "ImmoEliza" wants to create a machine learning model
to make price predictions on real estate sales in Belgium.
You must therefore create a dataset that holds the following columns :

Locality
Type of property (House/apartment)
Subtype of property (Bungalow, Chalet, Mansion, ...)
Price
Type of sale (Exclusion of life sales)
Number of rooms
Area
Fully equipped kitchen (Yes/No)
Furnished (Yes/No)
Open fire (Yes/No)
Terrace (Yes/No)
If yes: Area
Garden (Yes/No)
If yes: Area
Surface of the land
Number of facades
Swimming pool (Yes/No)
State of the building (New, to be renovated, ...)
You must save everything in a csv file.

Must-have features:
__________________
Data for all of Belgium.
Minimum 10 000 inputs
No empty row. If you are missing information, set the value to None.



"""

################################################
# 				Main
################################################

# -----------------------------------------------
# 		        Import
# -----------------------------------------------

from typing import List

import pandas as pd  # type: ignore

# ----------------------------------------------------
# 		        Globales
# ----------------------------------------------------


# -------------------------------------------------------
# 		        Modules or functions
# -------------------------------------------------------

#

# -------------------------------------------------------
# 				PROGRAMME
# -------------------------------------------------------


"""
Creating a csv file
"""
# Build dataframe


def initiate_panda():
    locality: List[str] = []
    type_property: List[str] = []
    subtype_property: List[str] = []
    price: List[int] = []
    type_sale: List[str] = []
    number_rooms: List[int] = []
    area: List[int] = []
    has_equiped_kitchen: List[int] = []
    is_furnished: List[int] = []
    has_open_fire: List[int] = []
    has_terrace: List[int] = []
    terrace_surface: List[int] = []
    has_garden: List[int] = []
    garden_surface: List[int] = []
    land_surface: List[int] = []
    facade_number: List[int] = []
    has_swimmingpool: List[int] = []
    building_state: List[str] = []

    data_dict = {
        "Locality": locality,
        "Type of property": type_property,  # House/apartment
        "Subtype of property": subtype_property,
        # Bungalow, Chalet, Mansion,..
        "Price": price,
        "Type of sale": type_sale,  # Exclusion of life sale
        "Number of rooms": number_rooms,
        "Area": area,
        "Fully equipped kitchen": has_equiped_kitchen,  # Yes/No
        "Furnished": is_furnished,  # Yes/No
        "Open fire": has_open_fire,  # Yes/No
        "Terrace": has_terrace,  # Yes/No
        "Area_terrace": terrace_surface,  # if Yes
        "Garden": has_garden,  # Yes/No
        "Area_garden": garden_surface,  # if Yes
        "Surface of the land": land_surface,
        "Number of facades": facade_number,
        "Swimming pool": has_swimmingpool,  # Yes/No
        "State of the building": building_state,
    }  # New, to be renovated, ...

    dataframe_house = pd.DataFrame(data_dict)

    return dataframe_house


def export_dataframe(data_dict):
    dataframe = pd.DataFrame(data_dict)
    dataframe.to_csv("dataframe2.csv")
