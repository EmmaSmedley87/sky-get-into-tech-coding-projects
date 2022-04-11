# this is a child class

from person import Person

class Customer(Person):

    def __init__(self, name, age, gender, customer_id, interest):
        super().__init__(name, age, gender)
        self.interest = interest
        self.customer_id = customer_id

    def introduction(self):
        print("I am ", self.name, "I am ", self.age, "I am interested in ", self.interest)

    def ask(self):
        question = input("What are you looking for? ")
        print(question)

    def satisfaction(self):
        response = input("Is this what you for looking for? Type YES or NO ")
        print(response)
        if response == "YES":
            print("I found what I wanted!")
        elif response == "No":
            print("This is not what i wanted")
        else:
            print(input("please choose either YES or No"))


