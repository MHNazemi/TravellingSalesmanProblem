__author__ = 'Nazemi'

import SharedCode
import random
import copy

class Ant:
    def __init__(self):
        self.pheromone =100

    def FindAPath(self,distances,pheromones):
        currentCityIndex=random.randint(0,len(distances))

        lenDistances=len(distances[currentCityIndex])
        probabilityDenominator=0
        for j in pheromones[currentCityIndex]:
            probabilityDenominator = probabilityDenominator + (pheromones[currentCityIndex][j]*((1/distances[currentCityIndex][j])**2))

        for i in lenDistances-1:
            del distances[currentCityIndex][currentCityIndex]
            randomIndex=random.uniform(0,probabilityDenominator)
            cumulativeProbability=0
            for k in distances[currentCityIndex]:
                cumulativeProbability= cumulativeProbability + (pheromones[currentCityIndex][k]*((1/distances[currentCityIndex][k])**2))
                if randomIndex < cumulativeProbability:
                    currentCityIndex = k
                    break
















def main():
    cities,distances=SharedCode.Cities()
    pheromones=[[1]*len(distances[0])]*len(distances)
    ant=Ant()
    ant.FindAPath(copy.copy(distances),copy.copy(pheromones))
    print(random.uniform(0,135.5))





if __name__=="__main__":main()