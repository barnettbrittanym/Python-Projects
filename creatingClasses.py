
#Creates a class, animals that gives general information about the animal in quiestion

class Animals:
    animal_name = 'No Name Provided'
    animal_genus= 'No genus Provided'
    animal_species= 'No species provided'

#Creates three child classes that all have the attributes of every animal, but their own unique attributes in addition.

class Dog(Animals):
    dog_breed: ' '
    color:''
    size:''

class Cat(Animals):
    cat_breed: ''
    color:''
    size:''
    demeanor:''

class Cow(Animals):
    cow_breed:''
    weight:''
    feed:''
    
