from utils.property import Property

url = "https://www.immoweb.be/fr/annonce/maison-de-maitre\
    /a-vendre/antwerpen/2600/9347744"


property = Property(url)
property.get_data()
print(property.locality)
