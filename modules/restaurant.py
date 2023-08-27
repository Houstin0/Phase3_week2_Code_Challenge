class Restaurant:
    def __init__(self,name):
        self.name=name

    @property    
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name

bulleys=Restaurant("bulleys") 
print(bulleys.name) 
   