from PIL import Image
from requests import get
from io import BytesIO
from datetime import date 
from os import mkdir

class Photo :
    """ It is the best photo struct I came up with.
        It reciveces the dict from the list of dicts in response json."""
        
    def __init__(self,metadata) :
        self.metadata = metadata
        self.id = metadata['id']
        self.width = metadata['width']
        self.height = metadata['height']
        self.url = metadata['url']
        self.photographer = metadata['photographer'] 
        self.photographer_url = metadata['photographer_url']
        self.photographer_id = metadata['photographer_id']
        self.alt = metadata['alt']

    @property
    def original(self):
        return self.metadata['src']['original']
    
    @property
    def large2x(self):
        return self.metadata['src']['large2x']

    @property
    def large(self):
        return self.metadata['src']['large']
    
    @property
    def medium(self):
        return self.metadata['src']['medium']
    
    @property
    def small(self):
        return self.metadata['src']['small']
    
    @property
    def portrait(self):
        return self.metadata['src']['portrait']
    
    @property
    def landscape(self):
        return self.metadata['src']['landscape']

    @property
    def wallpaper(self):
        return self.metadata['src']['original'] + "?auto=compress&cs=tinysrgb&dpr=1&h=1080&w=1920"
    

    def view(self):
        with Image.open(BytesIO(get(self.wallpaper , stream=True).content)) as img :
            img.show()
        
    def save(self,path):
        print(f"Saving '{self.alt}' ......",end="",sep="")
        with Image.open(BytesIO(get(self.wallpaper , stream=True).content)) as img :

            try :
                img.save(f"{path}/{date.today().strftime('%d-%m-%y')}/{self.alt}.png",'PNG')

            except FileNotFoundError :
                mkdir(f"{path}/{date.today().strftime('%d-%m-%y')}/")
                img.save(f"{path}/{date.today().strftime('%d-%m-%y')}/{self.alt}.png",'PNG')

            finally :
                print("Saved.")