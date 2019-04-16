#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Function:
    
    def __init__(self,result,powU,powW,powX,powY,powZ,
                         powU1,powW1,powX1,powY1,powZ1,
                         powU2,powW2,powX2,powY2,powZ2,
                         powU3,powW3,powX3,powY3,powZ3,
                         powU4,powW4,powX4,powY4,powZ4):
        self.result=result
        self.powU=powU
        self.powW=powW
        self.powX=powX
        self.powY=powY
        self.powZ=powZ
        self.powU1=powU1
        self.powW1=powW1
        self.powX1=powX1
        self.powY1=powY1
        self.powZ1=powZ1
        self.powU2=powU2
        self.powW2=powW2
        self.powX2=powX2
        self.powY2=powY2
        self.powZ2=powZ2
        self.powU3=powU3
        self.powW3=powW3
        self.powX3=powX3
        self.powY3=powY3
        self.powZ3=powZ3
        self.powU4=powU4
        self.powW4=powW4
        self.powX4=powX4
        self.powY4=powY4
        self.powZ4=powZ4
    
    def getResult(self):
        return self.result
        
    def getFunction(self):
        print(f"u**{self.powU}*w**{self.powW}*x**{self.powX}*y**{self.powY}*z**{self.powZ}+u**{self.powU1}*w**{self.powW1}*x**{self.powX1}*y**{self.powY1}*z**{self.powZ1}+u**{self.powU2}*w**{self.powW2}*x**{self.powX2}*y**{self.powY2}*z**{self.powZ2}+u**{self.powU3}*w**{self.powW3}*x**{self.powX3}*y**{self.powY3}*z**{self.powZ3}+u**{self.powU4}*w**{self.powW4}*x**{self.powX4}*y**{self.powY4}*z**{self.powZ4}")
        
    def calculateFunction(self,u,w,x,y,z):
        return u**self.powU*w**self.powW*x**self.powX*y**self.powY*z**self.powZ+u**self.powU1*w**self.powW1*x**self.powX1*y**self.powY1*z**self.powZ1+u**self.powU2*w**self.powW2*x**self.powX2*y**self.powY2*z**self.powZ2+u**self.powU3*w**self.powW3*x**self.powX3*y**self.powY3*z**self.powZ3+u**self.powU4*w**self.powW4*x**self.powX4*y**self.powY4*z**self.powZ4


# In[29]:


import random

FROM=-100
TO=100

class Individual:
    def __init__(self,function):
        self.x=random.randint(FROM,TO)
        self.y=random.randint(FROM,TO)
        self.z=random.randint(FROM,TO)
        self.u=random.randint(FROM,TO)
        self.w=random.randint(FROM,TO)
        self.function=function
        self.probability=0
        self.fa=abs(function.calculateFunction(self.u,self.w,self.x,self.y,self.z-function.getResult()))

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    def getU(self):
        return self.u
    
    def getW(self):
        return self.w
                    
    def getFa(self):
        return self.fa
    
    def getProbability(self):
        return self.probability
    
    def setX(self,x):
        self.x=x
        
    def setY(self,y):
        self.y=y
        
    def setZ(self,z):
        self.z=z
        
    def setU(self,u):
        self.u=u
        
    def setW(self,w):
        self.w=w
    
    def setFa(self):
        self.fa=abs(self.function.calculateFunction(self.u,self.w,self.x,self.y,self.z-self.function.getResult()))
    
    def setProbability(self,p):
        self.probability=p
        
    def increaseProbability(self,i):
        self.probability=self.probability*i
                    
    def __str__(self):
        return "(%d,%d,%d,%d,%d); fa=%d" % (self.u,self.w,self.x,self.y,self.z,self.fa)


# In[30]:


POPULATION_SIZE=100
SELECTION=40
NUMBER_OF_SELECTION=10
MAX_REPEAT=100
PROBABILITY_OF_MUTATION_WHILE_NUCLEAR_BLAST=0.75
PROBABILITY_OF_MUTATION_MOST_SUITABLE = 0.15
PROBABILITY_OF_MUTATION_LEAST_SUITABLE = 0.07
SUITABLE = 20

class Population:
    
    def __init__(self,function):
        self.function=function
        self.population=[Individual(self.function) for i in range(POPULATION_SIZE)]
        self.numberOfGeneration=0
        self.mutationMostSuitable=PROBABILITY_OF_MUTATION_MOST_SUITABLE
        self.mutationLeastSuitable=PROBABILITY_OF_MUTATION_LEAST_SUITABLE
    
    def calculateProbabilityForElement(self,element,elements):
        probability=1/element.getFa()
        denominator=0
        for i in range(len(elements)):
            denominator=denominator+1/elements[i].getFa()
        if denominator==0:
            denominator=1
        probability=probability/denominator
        element.setProbability(probability)
        elements[0].setProbability(probability)
        j=1
        for j in range(len(elements)):
            nextProbability = elements[j].getProbability(probability)
            probability += nextProbability
            elements[j].setProbability(probability)
    
    def crossbreeding(self,firstparant,secondparent):
        kid=Individual(self.function)
        #u
        randomSelect=random.randint(1,2)
        if randomSelect == 1:
            kid.setU(firstparant.getU())
        else:
            kid.setU(secondparent.getU())
        #w
        randomSelect=random.randint(1,2)
        if randomSelect == 1:
            kid.setW(firstparant.getW())
        else:
            kid.setW(secondparent.getW())
        #x
        randomSelect=random.randint(1,2)
        if randomSelect == 1:
            kid.setX(firstparant.getX())
        else:
            kid.setX(secondparent.getX())
        #y
        randomSelect=random.randint(1,2)
        if randomSelect == 1:
            kid.setY(firstparant.getY())
        else:
            kid.setY(secondparent.getY())
        #z
        randomSelect=random.randint(1,2)
        if randomSelect == 1:
            kid.setZ(firstparant.getZ())
        else:
            kid.setZ(secondparent.getZ())
        
         
        kid.setFa()
        return kid
    
    def mutateMostSuitable(self,individual):
        issomethingchange = False
        temp = random.random()
        if temp<=self.mutationMostSuitable:
            issomethingchange=True
            individual.setU(FROM+random.randint(0,TO-FROM+1))    
            
        if temp<=self.mutationMostSuitable:
            issomethingchange=True
            individual.setW(FROM+random.randint(0,TO-FROM+1))    
            
        if temp<=self.mutationMostSuitable:
            issomethingchange=True
            individual.setX(FROM+random.randint(0,TO-FROM+1))    

        if temp<=self.mutationMostSuitable:
            issomethingchange=True
            individual.setY(FROM+random.randint(0,TO-FROM+1))
                
        if temp<=self.mutationMostSuitable:
            issomethingchange=True
            individual.setZ(FROM+random.randint(0,TO-FROM+1)) 
        
        if issomethingchange:
            individual.setFa()
            
    def mutateLeastSuitable(self,individual):
        issomethingchange = False
        temp = random.random()
        if temp<=self.mutationLeastSuitable:
            issomethingchange=True
            individual.setU(FROM+random.randint(0,TO-FROM+1))
        if temp<=self.mutationLeastSuitable:
            issomethingchange=True
            individual.setW(FROM+random.randint(0,TO-FROM+1))
        if temp<=self.mutationLeastSuitable:
            issomethingchange=True
            individual.setX(FROM+random.randint(0,TO-FROM+1))
        if temp<=self.mutationLeastSuitable:
            issomethingchange=True
            individual.setY(FROM+random.randint(0,TO-FROM+1))
        if temp<=self.mutationLeastSuitable:
            issomethingchange=True
            individual.setZ(FROM+random.randint(0,TO-FROM+1))
            
        if issomethingchange:
            individual.setFa()
        
    def replacegeneration(self,allpopulation):
        numberinnewgeneration=0
        newgeneration=[]
        allpopulation.sort(key=lambda x: x.probability)
        while numberinnewgeneration<=POPULATION_SIZE:
            for i in range(len(allpopulation)):
                self.calculateProbabilityForElement(allpopulation[i],allpopulation)
                allpopulation[i].increaseProbability(10**11)
            temp = random.uniform(0,10**11)
            for j in range(1,len(allpopulation)):
                if allpopulation[j-1].getProbability()<temp and temp<=allpopulation[j].getProbability():
                    newgeneration.append(allpopulation[j])
                    allpopulation.pop(j)
                    break
            newgeneration.append(allpopulation[0])
            numberinnewgeneration=numberinnewgeneration+1
        return newgeneration
    
    def getNewPopulation(self):
        #Селекция
        selectedfromoldgeneration=[]
        self.population.sort(key=lambda x: x.fa)
        for i in range(SELECTION):
            selectedfromoldgeneration.append(self.population[i])
        #Скрещивание
        childrens=[]
        for start in range(len(selectedfromoldgeneration)-1):
            for number in range(NUMBER_OF_SELECTION):
                selectedIndex=random.randint(0,len(selectedfromoldgeneration)-1)
                while selectedIndex==start:
                    selectedIndex=random.randint(0,len(selectedfromoldgeneration)-1)
                childrens.append(self.crossbreeding(selectedfromoldgeneration[start],selectedfromoldgeneration[selectedIndex]))
        #Мутация
        self.population.sort(key=lambda x: x.fa)
        for j in range(SUITABLE+1):
            self.mutateMostSuitable(childrens[j])
        for k in range(SUITABLE+1, len(childrens)):
            self.mutateLeastSuitable(childrens[k])
        #Замещение
        self.population.sort(key=lambda x: x.fa)
        childrens.sort(key=lambda x: x.fa)
        new = []
        m = 21
        for m in range (len(self.population)):
            new.append(self.population[m])
        for n in range (21):
            new.append(childrens[n])
        return new
            
        
    def run(self):
        repeat=0
        isNuclearBlast=False
        self.population.sort(key=lambda x: x.fa)
        self.bestfromall=self.population[0]
        self.bestfromthisgeneration=self.population[0]
        while 1:
            if self.bestfromthisgeneration.getFa()==0:
                break
            if repeat>MAX_REPEAT:
                isNuclearBlast=True
                self.mutationLeastSuitable=PROBABILITY_OF_MUTATION_WHILE_NUCLEAR_BLAST
                self.mutationMostSuitable=PROBABILITY_OF_MUTATION_WHILE_NUCLEAR_BLAST-0.1
            print("Поколение номер ",self.numberOfGeneration+1,end="")
            newpopulation=self.getNewPopulation()
            self.population.clear()
            for j in range(len(newpopulation)):
                self.population.append(newpopulation[j])
            self.population.sort(key=lambda x: x.fa)
            self.bestfromthisgeneration=self.population[0]
            if self.bestfromthisgeneration.getFa()<self.bestfromall.getFa():
                self.bestfromall=self.bestfromthisgeneration
                repeat=0
            else:
                repeat=repeat+1
            print(f" Лучший из всех поколений: {self.bestfromall}",
                  f" Лучший из {self.numberOfGeneration+1} покаления: {self.bestfromthisgeneration}")
            if isNuclearBlast:
                self.mutationMostSuitable=PROBABILITY_OF_MUTATION_MOST_SUITABLE
                self.mutationLeastSuitable=PROBABILITY_OF_MUTATION_LEAST_SUITABLE
                repeat=0
            self.numberOfGeneration=self.numberOfGeneration+1
        print(f"Решение {self.bestfromall} и количество поколений {self.numberOfGeneration+1}")


# In[35]:


f=Function(-5,0,2,1,2,1,0,2,2,2,1,2,1,1,0,0,0,2,2,2,2,0,0,0,1,1)
p=Population(f)
p.run()


# In[71]:


f=Function(40,0,0,1,1,2,0,0,0,1,0,1,2,1,2,0,0,0,1,1,2,2,1,2,1,1)
p=Population(f)
p.run()


# In[74]:


f=Function(-50,0,0,0,0,1,1,0,1,1,0,0,2,1,0,2,0,1,2,0,2,2,0,2,1,2)
p=Population(f)
p.run()


# In[76]:


f=Function(-5,0,2,1,2,1,0,2,2,2,1,2,1,1,0,0,0,2,2,2,2,0,0,0,1,1)
p=Population(f)
p.run()


# In[78]:


f=Function(22,0,2,0,0,1,1,0,0,0,2,0,0,0,2,0,1,1,2,2,2,0,1,0,1,1)
p=Population(f)
p.run()


# In[80]:


f=Function(40,2,2,2,0,0,0,1,2,1,0,1,0,0,1,0,1,1,2,1,1,1,1,2,2,0)
p=Population(f)
p.run()

