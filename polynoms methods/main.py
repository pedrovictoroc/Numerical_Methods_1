from find_roots import *

factors = []

#First things first, I will explain the polynom abstraction i used

#To represent an polynom like X⁴ - 10x³ + 35x² - 50x + 24
#we will transform the equation in a list, ordered by the index of X
#the right represent of this polynom is: [24,-50,35,-10,1]
#where X⁰ coeficient are in the 0º position of the list, X¹ in the 1º, same for the rest

#Some examples to test:

#x = [-105,71,-15,1]
#x = [-64,56,-14,1]
#x = [-6,11,-6,1]
#x = [24,-50,35,-10,1]

roots = find_roots(x)