# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:54:39 2024

@author: miche
"""

#import numpy as np
#FoodType = str(input("Do you want to cook breakfast, lunch, or dinner? "))

veggies = []
fruits = []
meat = []
grains = []

def getIngredList(listType,foodType):
    counter = 0
    if foodType != 0:
        while counter < foodType:
            getItem = input("Enter food item: ")
            listType.append(getItem)
            counter += 1

        
def askIngredients():
    askFruits = int(input("Enter number of fruits: "))
    getIngredList(fruits,askFruits)
    askVeggies = int(input("Enter number of vegetables: "))
    getIngredList(veggies, askVeggies)
    askProtein = input("Enter type of meat, or enter none: ")
    if askProtein != 'none':
        meat.append(askProtein)
    askGrain = input('Enter type of bread/grain, or enter none: ')
    if askGrain != 'none':
       grains.append(askGrain)
           

mealType = input("Do you want to cook a dish for breakfast, lunch, or dinner?")

if mealType == "Breakfast":
    askIngredients()
    if len(meats) > 0 and len(grains) > 0:
        print("Make a sandwich!")
    
    
