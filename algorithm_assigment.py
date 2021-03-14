#!/usr/bin/env python3
import numpy as np

class MyClass(object):
    def __init__(self):
        # Extracting values from the file
        lines = []
        f = open("./data_cases/case_01.in", "r")
        lines = f.readlines()
        self.first_line = [int(i) for i in lines[0].split(" ")]
        self.links = np.zeros([self.first_line[0],2])
        for i in range(1, self.first_line[0] + 1):
            nums_fila = [int(j) for j in lines[i].split(" ")]
            self.links[i-1,0] = nums_fila[0]
            self.links[i-1,1] = nums_fila[1]
        self.reds_line = [int(i) for i in lines[len(lines)-2].split(" ")] 
        self.blues_line = [int(i) for i in lines[len(lines)-1].split(" ")]

        # Variables for the algorithm
        self.link_ways = (np.zeros([self.first_line[0],4]) - 1)
        self.link_states = np.zeros([self.first_line[0],4])
        self.flagRB = True
        self.flagInit = True

    # Main functions
    def graphWaysConstruction(self):
        for i in range(0,self.first_line[0]):
            for j in range(0,self.first_line[0]):
                if i != j:
                    x = 0.1
                    if self.links[i,0] == self.links[j,0] or self.links[i,0] == self.links[j,1]:
                        if self.links[i,0] == self.links[j,1]: x = 0.2
                        if self.link_ways[i,0] == -1 : self.link_ways[i,0] = j + x
                        elif self.link_ways[i,1] == -1 : self.link_ways[i,1] = j + x
                    if self.links[i,1] == self.links[j,0] or self.links[i,1] == self.links[j,1]:
                        if self.links[i,1] == self.links[j,1]: x = 0.2
                        if self.link_ways[i,2] == -1 : self.link_ways[i,2] = j + x
                        elif self.link_ways[i,3] == -1 : self.link_ways[i,3] = j + x
    def linkStatesCalculation(self):
        print(self.markLink(self.findColor(self.reds_line[0])))

        print(self.links)
        print(self.link_ways)
        print(self.link_states)

    # Secondary functions
    def findColor(self,value):
        position = np.where(self.links[:,0] == value)[0]
        if len(position) > 0 : 
            return np.ndarray.item(position + 0.1)
        else: 
            position = np.where(self.links[:,1] == value)[0]
            return np.ndarray.item(position + 0.2)
    def position(self,value):
        value -= 0.1
        row = value // 1
        col =  round(value % 1, 2) * 10
        return [row,col]
    def markLink(self,value):
        rowcol = self.position(value)

        if self.flagInit == False and ((rowcol[1] == 0 and self.link_ways[int(rowcol[0]),0] == -1 and self.link_ways[int(rowcol[0]),1] == -1)
        or (rowcol[1] == 1 and self.link_ways[int(rowcol[0]),2] == -1 and self.link_ways[int(rowcol[0]),3] == -1)):
            print("End")
        else:
            print("Marked")
            flagInit = False

            direction = rowcol[1]
            if self.flagRB == False: direction += 2 
            print(int(rowcol[0]),int(direction))
            self.link_states[int(rowcol[0]),int(direction)] = 1
            
            if rowcol[1] == 0:
                if self.link_ways[int(rowcol[0]),2] != -1: self.markLink(self.link_ways[int(rowcol[0]),2])
                if self.link_ways[int(rowcol[0]),3] != -1: self.markLink(self.link_ways[int(rowcol[0]),3])
            else:
                if self.link_ways[int(rowcol[0]),0] != -1: self.markLink(self.link_ways[int(rowcol[0]),0])
                if self.link_ways[int(rowcol[0]),1] != -1: self.markLink(self.link_ways[int(rowcol[0]),1])
            
        


a = MyClass()
a.graphWaysConstruction()
a.linkStatesCalculation()



