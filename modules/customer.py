from review import Review
class Customer:

    customers=[]
   
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.review=[]
        self.restaurants=[]
        Customer.add_customer(self)
        self.add_restaurants()

    def given_name(self):
        print (self.first_name)   
        return self.first_name 
    def family_name(self):
        print(self.last_name)
        return self.last_name  
    def full_name(self):
        print (f"{self.first_name} {self.last_name}") 
        return f"{self.first_name} {self.last_name}"               
         

    @classmethod
    def add_customer(cls,customer):
        cls.customers.append(customer)
    @classmethod
    def all(cls):
        print (cls.customers)                   
        return cls.customers  

    def add_restaurants(self):
        for rev in Review.reviews:
            if rev["customer"] == self.first_name:
                self.restaurants.append(rev["restaurant"])

    def add_review(self,restaurant,rating):
        Review(self.first_name,restaurant,rating)

    def num_reviews(self):
        return len(self.restaurants)  

    @classmethod
    def find_by_name(cls,name):
        for customer in cls.customers:
            if customer.full_name() == name:
                found=customer
                break
        return found 
    @classmethod
    def find_all_by_given_name(cls,name):
        found=[]
        for customer in cls.customers:
            if customer.given_name() == name:
                found.append(customer)
        return found        
            
john=Customer("john","doe") 
mary=Customer("mary","jane")
ken=Customer("ken","johns")
Customer.find_all_by_given_name("jane")





  # def get_given_name(self):   
    #     return self.first_name 
    # def set_given_name(self,first_name):
    #     if isinstance(first_name,str):
    #         self.first_name=first_name

    # given_name=property(get_given_name,set_given_name,)  

    # def get_family_name(self):
    #     return self.family_name
    # def set_family_name(self,family_name):
    #     if isinstance(family_name,str):
    #         self.last_name=family_name
    # family_name=property(get_family_name,set_family_name,)