# import statistics module
import statistics

class Person:

    # constructor with 2 parameters
    def __init__(self,name,age):
    # assign parameters to private variables
        self.__name = name
        self.__age = age

    # method to get person age
    def get_age(self):
        return self.__age

# method to return tuple of mean, median, mode
def basic_stats(persons):

# to store all persons age
    ages = []

# loop for persons
    for person in persons:
# call methhod get_age for person and
# ages add to list
        ages.append(person.get_age())

    # calculate mean, median, mode using statistics module
    mean = statistics.mean(ages)
    median = statistics.median(ages)
    mode = statistics.mode(ages)

    # return tuple of mean, median, mode
    return (mean,median,mode)

# Testing code
# Creating Person class objects
a = Person("Person1",10)
b = Person("Person2",25)
c = Person("Person3",5)
d = Person("Person4",44)
e = Person("Person5",22)
f = Person("Person6",27)
g = Person("Person7",17)
h = Person("Person8",25)

# create list of person objects
persons = [a,b,c,d,e,f,g,h]

# call basic_stats to get tuple of stats
values = basic_stats(persons)

# print values
print("Mean Median Mode")
print(values)
