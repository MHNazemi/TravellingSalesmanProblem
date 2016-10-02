__author__ = 'Nazemi'

import SharedCode
import random
import copy

class Ant:
    def __init__(self):
        self.pheromone =100

    def FindAPath(self,distances,pheromones):
        currentCityIndex=random.randint(0,len(distances)-1)
        path=[]

        lenDistances=len(distances[currentCityIndex])

        lengthTour=0
        selectedIndex=[0]*len(distances[currentCityIndex])

        for i in range(0,lenDistances-1):
            selectedIndex[currentCityIndex]=1


            probabilityDenominator=0
            for j in range(0,len(pheromones[currentCityIndex])):
                if j!=currentCityIndex and selectedIndex[j]!=1:
                    probabilityDenominator = probabilityDenominator + (pheromones[currentCityIndex][j]*((1/distances[currentCityIndex][j])**2))

            randomIndex=random.uniform(0,probabilityDenominator)

            cumulativeProbability=0


            for k in range(0,lenDistances):



                if selectedIndex[k]==1:
                    continue
                if currentCityIndex!=k:
                    cumulativeProbability= cumulativeProbability + (pheromones[currentCityIndex][k]*((1/distances[currentCityIndex][k])**2))

                if randomIndex <= cumulativeProbability:

                    lengthTour = lengthTour+ distances[currentCityIndex][k]
                    path.append([currentCityIndex,k])
                    currentCityIndex = k
                    break
        return path , lengthTour
















def PheromonesUpdate(_solutions,_pheromones):

    allMovements=[]
    for path in _solutions:
        for movement in path[0]:
            allMovements.append([movement,path[1]])

    for x in range(0,len(_pheromones)):
        for y in range(0, len(_pheromones[x])-x):

            count=0
            for move in allMovements:
                if (move[0] == [x,y] )or (move[0] == [y,x]) :
                    count = count + (100/move[1])

            _pheromones[x][y]=((1-0.02)*_pheromones[x][y])+count
            _pheromones[y][x]=_pheromones[x][y]

    return _pheromones




def main():
    antCount=50
    iteration=100

    cities,distances=SharedCode.Cities()
    pheromones=[[1]*len(distances[0])]*len(distances)


    mins=[10000000000]*iteration
    for a in range(0,iteration):
        solutions=[]
        for i in range(0,antCount):
            ant=Ant()
            solution,length= ant.FindAPath(copy.copy(distances),copy.copy(pheromones))
            newSolu=[]
            newSolu.append(solution)
            newSolu.append(length)
            solutions.append(newSolu)

            if length<mins[a]:
                mins[a]=length


        pheromones=PheromonesUpdate(copy.copy(solutions),pheromones)


    print(mins)



if __name__=="__main__":main()