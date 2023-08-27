from review import Review
class Restaurant:
    def __init__(self,name):
        self._name=name
        self.reviews=[]
        self.customers=[]
        self.add_reviews()
        self.add_customers()

    @property    
    def get_name(self):
        return self._name
    @property
    def set_name(self,name):
        self._name=name

    def add_reviews(self):
        for re in Review.reviews:
            if re["restaurant"] == self._name:
                self.reviews.append(re)
    def add_customers(self):
        customer_list= [rev["customer"] for rev in self.reviews]
        self.customers.append(customer_list)            
                
               
bulleys=Restaurant("bulleys") 

   