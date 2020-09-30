# Author: Satish Clarke
# Date: 9/29/2020
# Description: CS 162 1st assignment - The purpose of this program is to import
# the module named statistics in order to generate mean, median, and mode for a
# list of given people.




# import statistics module
import statistics


class Person:
    '''
    A class to represent a person.

    Attributes
    ----------
    name : str
        Name of the person
    age : int
        Age of the person
    '''

    def __init__(self, name, age):
        '''
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                First name of the person
            age : int
                Age of the person
        '''

        self.__name = name
        self.__age = age

    def get_age(self):
        '''
        Prints the person's name and age.

        Returns
        -------
        self.__age '''

        return self.__age


def basic_stats(persons):
    '''
    Accepts a list of users. Returns the mean, median, mode of the ages of
    the given users.

        Parameters:
            persons : List of int

        Returns:
            mean (float): The mean value of all ages of the given users.
            median (float): The median value of the ages of the given users.
            mode (float): The mode value of all ages of the given users.
    '''

# The list that stores all persons age
    ages = []

# Loop for persons - contains call method get_age for person & ages add to list
    for person in persons:
        ages.append(person.get_age())

# Here we calculate the mean, median, mode via the statistics module
    mean = statistics.mean(ages)
    median = statistics.median(ages)
    mode = statistics.mode(ages)

# Returns a tuple of the mean, median, mode
    return (mean, median, mode)

# This is the list of person objects
persons = [a, b, c, d, e, f, g, h]

# Calling basic_stats in order to get tuple of stats
values = basic_stats(persons)

# print values
print("Mean Median Mode")
print(values)
