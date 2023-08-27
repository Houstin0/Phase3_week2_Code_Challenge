class Review:
    reviews=[]
    def __init__(self,customer,restaurant,rating):
        self._customer=customer
        self._restaurant=restaurant
        self._rating=rating
        self.store_review()                             
        Review.add_review(self.review_dict)

    def store_review(self):
        self.review_dict={
            "customer":self._customer,
            "restaurant":self._restaurant,
            "rating":self._rating
        }
        return self.review_dict

    @property
    def customer(self):
        return self._customer
    @property
    def restaurant(self):
        return self._restaurant    
    def rating(self):
        return self._rating
    
    @classmethod
    def add_review(cls,review):
        cls.reviews.append(review)
    @classmethod
    def all(cls):
        print(cls.reviews)
        return cls.reviews    
    
joe=Review("joe","hilton","5")
mary=Review("mary","bulleys",7)

# print(Review.reviews) 