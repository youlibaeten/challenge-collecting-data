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
The real estate company "ImmoEliza" wants to create a machine learning model to make price predictions on real estate sales in Belgium.
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

import pandas as pd

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

locality = []
type_property = []
subtype_property = []
price = []
type_sale = []
number_rooms = []
area = []
has_equiped_kitchen = []
is_furnished = []
has_open_fire = []
has_terrace = []
terrace_surface = []
has_garden = []
garden_surface = []
land_surface = []
facade_number = []
has_swimmingpool = []
building_state = []


data_dict = {
    "Locality": locality,
    "Type of property": type_property,  # House/apartment
    "Subtype of property": subtype_property,  # Bungalow, Chalet, Mansion,..
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


dataframe_house.to_csv("dataframe2.csv")
