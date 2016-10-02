__author__ = 'Nazemi'
from math import *

class City:
    def __init__(self,x,y):
        self.x=x
        self.y=y



def GetDistance(firstCity,secondCity):
    yDistance=abs(int(firstCity.y)-int(secondCity.y))
    xDistance=abs(int(firstCity.x)-int(secondCity.x))
    return sqrt(pow(yDistance,2)+pow(xDistance,2))


def ReadCities(file):
    file=open(file)
    cities=[]
    for line in file.readlines():
        x,y=line.split('-')
        cities.append(City(x,y))
    return cities

def MakeDistanceMatrix(cities):
    distance=[]
    distances=[]
    for city in cities:
        distance=[]
        for otherCity in cities:
            distance.append(GetDistance(city,otherCity))
        distances.append(distance)

    return distances

def Cities(file='Cities.txt'):
    cities=ReadCities(file)
    return cities,MakeDistanceMatrix(cities)