import requests as req
from util.Photo import Photo

class API :
    """It is a basic inteface for an API object."""

    def __init__(self , key:str , orientation = "landscape" , Image_per_page = 10 , pages=1 ):
        self.Auth = {"Authorization": key }
        self.request = None
        self.json = None
        self.orientation = orientation
        self.Images_per_page = Image_per_page
        self.pages = pages
    
    def search(self):
        tags = input("Enter your search tags : ").replace(" ", "+")
        url = f"https://api.pexels.com/v1/search?query={tags}&orientation={self.orientation}&per_page={self.Images_per_page}&page={self.pages}"
        self._request(url)

    def _request(self, url):
        try :
            self.request = req.get(url, timeout = 20, headers=self.Auth)
        
            if self.request.ok :
                self.json = self.request.json()
            else :
                print(f"Connection Error, Check your API Key and try again.")
                print(f"API Key is " + self.Auth['Authorization'])
                exit()

        except :
            print(f"Connection Error , Check your internet connection and try again.")
            exit()
    
    def get_photos(self):
        return [Photo(photo) for photo in self.json["photos"]]