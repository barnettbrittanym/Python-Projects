#Creates a class with a private attribute
class Nerd:
        _name="Randolf"
        _score= 400

        def displayGameScore(self):
            print("Name: ", self._name)
            print("Score: ", self._score)
            
#Creates an object from a private attribute
obj = Nerd()
obj.displayGameScore()

#Creates a class with a protected attribute
class Geek:
        __fname = "Brittany"
        __lname = "Barnett"

        def displayFullName(self):
            print("Name: {} {}".format(self.__fname, self.__lname))
            
#Creates an object from a protected attribute
obj = Geek()
obj.displayFullName()

    

