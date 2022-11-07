from util.API import API 


PEXELS_API_KEY = ""

on = True

api = API(PEXELS_API_KEY)

while on : 

    api.search()

    Photos = api.get_photos()

    for Photo in Photos:

        Photo.save("Wallpapers")
    

    if input("\nDo you wish to continue? (y/n): ").lower() == "n" :

        on = False 
