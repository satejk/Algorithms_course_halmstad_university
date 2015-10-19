__author__ = 'satej'

import networkx as nx
from networkx_viewer import Viewer
import collections
import math as m

from random import randint

fh = open("cities.txt","r")

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


print "reading file"
read_line = fh.read()
graph_input = read_line.split()
print graph_input

G = nx.Graph()

print "starting loop"
i = 0
graph_input_lenght =  len(graph_input)
while i < (range(graph_input_lenght)):
    print "adding edge"
    a =  graph_input[i]
    b =  graph_input[i + 1]
    wt =  graph_input[i+2]

    G.add_edge(a,b,weight=wt)
    print
    i = i + 3
    if i == graph_input_lenght:
        break

print "graph created"


def breadth_first_search(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    tour = []
    visited[start] = True
    tour.append(start)
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
                tour.append(next)
    tour.append(start)
    return tour
tour = breadth_first_search(G, 'lulea')
print tour
print G.edge['lulea']['ostersund']['weight']

"""
###############################################################################################

#funtions


def distance(G, list):
    dist = 0

    while ():

        a = list[i]
        b = list[i+1]

        dist = dist + G.graph[a][b]['weight']

        if(i == (len(list) - 1)):
            break

        i = i + 1

    return dist


def tour():
    pass


def acceptance_probablity(new_energy, current_energy, temp):

    if (new_energy < current_energy):
        return 1

    else:
        value = (new_energy - current_energy) / temp
        return m.exp(value)



###############################################################################################3

#simulated annealing

#set temperature
temp = 10000

#set cooling rate
cooling = 0.003


#generate initial tour
#and set current solution as tour

current_solution = tour()

#set current tour as best
best = current_solution

while(temp > 1):


    new_solution = tour()

    #get random positions in the tour
    r_a = randint(0,len(current_solution))
    r_b = randint(0,len(new_solution))


    #get cities at those postions
    curent_swap_city = current_solution[r_a]
    new_swap_city = new_solution[r_b]

    #swap the cities
    current_solution[r_a] = new_swap_city
    new_solution[r_b]  = curent_swap_city


    #get energy i.e the total distance of the current and new solutions
    current_distance  = distance(current_solution)
    new_solution = distance(new_solution)

    #decide if we should accept the new solution or keep the old one
    if (acceptance_probablity(current_distance, new_solution, temp) > m.random()):
        currentSolution = new_solution


    #keep track of the best solution
    #if (current_distance < best_distance):
    best = current_solution



    #cool the system

    temp  *= 1-cooling


#################################################################################################3

"""



app = Viewer(G)

app.mainloop()

fh.close()
