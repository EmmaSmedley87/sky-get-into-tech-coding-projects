# this is a child class

class Employee:
    def __init__(self, name, age, gender, store, department, position):
        super().__init__(name, age, gender)
        self.store = store
        self.department = department
        self.position = position

    def ask_store(self):
        exit = "X"
        while exit != "X":
            question = input("What store would you like to purchase this from?")
            if self.store == question:
                print(question(input("Follow me, i'll take you to ", question)))
            else:
                print("Im sorry, this is the wrong store.")
                print(input("Would you like too see", store, "instead."))


    def ask_brand(self):
        question = input("What brands do you stock these skirts in?")
        print(question(input("Here is a list of the brand ")))

    # def ask(self):
    #     question = input("What are you looking for? ")
    #     print(question)