import math
import threading
import time

from utils.create_dataset import export_dataframe
from utils.property import Property

urls = []
urls.append(
    "https://www.immoweb.be/fr/annonce/maison-de-maitre\
    /a-vendre/antwerpen/2600/9347744"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/maison/a-vendre\
        /uccle/1180/9310971?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/maison/a-vendre\
        /wemmel/1780/9348673?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/maison-de-maitre\
        /a-vendre/woluwe-saint-lambert/1200/9135743?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /gand/9000/9347068?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /wellin/6920/9346924?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/maison/a-vendre\
        /nivelles/1400/9346951?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.imm4oweb.be/fr/annonce/appartement/a-vendre\
        /gand/9000/9346747?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /gand/9000/9346707?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /ixelles/1050/9346804?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /ixelles/1050/9351513?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /ixelles/1050/9351511?searchId=60af45e77ea2c"
)
urls.append(
    "https://www.immoweb.be/fr/annonce/appartement/a-vendre\
        /schaerbeek/1030/9351516?searchId=60af45e77ea2c"
)


def test_thread(url, property_list):
    try:
        property = Property(url)
        property.get_data()
        data_dict = {
            "Locality": property.locality,
            "Type of property": property.property_type,
            "Subtype of property": property.property_subtype,
            "Price": property.price,
            "Type of sale": property.sale_type,
            "Number of rooms": property.rooms,
            "Area": property.area,
            "Fully equipped kitchen": property.is_kitchen_equipped,
            "Furnished": property.is_furnished,
            "Open fire": property.has_open_fire,
            "Terrace": property.has_terrace,
            "Area_terrace": property.terrace_surface,
            "Garden": property.has_garden,
            "Area_garden": property.garden_surface,
            "Surface of the land": property.land_surface,
            "Number of facades": property.facade_number,
            "Swimming pool": property.has_swimming_pool,
            "State of the building": property.property_state,
        }
        property_list.append(data_dict)
    except Exception as ex:
        print(ex)


def process_urls(urls):
    start_time = time.time()
    property_list = []
    threads = []
    for url in urls:
        t = threading.Thread(target=test_thread, args=(url, property_list))
        t.start()
        threads.append(t)

    for x in threads:
        x.join()

    time_in_seconds = time.time() - start_time
    print(
        f"Process finished --- {math.floor((time_in_seconds/60))} \
min {math.floor(time_in_seconds % 60)} seconds --- \
        \nNumber of threads: {len(threads)}"
    )

    export_dataframe(property_list)

    return property_list


list = []
list = process_urls(urls)
print(len(list))
