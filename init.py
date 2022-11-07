from util.API import API 


PEXELS_API_KEY = "563492ad6f91700001000001f29e8c757b224c5ab116bca75da75c46"

on = True

api = API(PEXELS_API_KEY)

while on : 

    api.search()

    Photos = api.get_photos()

    for Photo in Photos:

        Photo.save("Wallpapers")
    

    if input("\nDo you wish to continue? (y/n): ").lower() == "n" :

        on = False 
