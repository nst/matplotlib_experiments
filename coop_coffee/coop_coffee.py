#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import genfromtxt
from matplotlib import pyplot
from pylab import Rectangle

data = genfromtxt('coop_coffee.csv', dtype=None, delimiter='\t')

x = []
y = []
colors = []

for row in data:

    name = row[3].lower()
    
    if 'pièces' in name or \
       'portions' in name or \
       'sachet' in name or \
       'capsule' in name or \
       'Nescafé Dolce Gusto' in name:
        colors.append('yellow')
    elif 'soluble' in name or 'instantané' in name:
        colors.append('red')
    elif 'grains' in name:
        colors.append('green')
    elif 'moulu' in name:
        colors.append('brown')
    else:
        colors.append('lightGray')
    
    x.append(row[0]) # price
    y.append(row[1]) # weight

pyplot.title("Coffee, Coop, July 2012")
pyplot.xlabel("Price [CHF]")
pyplot.ylabel("Weight [Kg]")

sct = pyplot.scatter(x, y, marker='o', color=colors)
sct.set_alpha(0.25)

p1 = Rectangle((0, 0), 1, 1, fc="yellow")
p2 = Rectangle((0, 0), 1, 1, fc="red")
p3 = Rectangle((0, 0), 1, 1, fc="green")
p4 = Rectangle((0, 0), 1, 1, fc="brown")
pyplot.legend((p1, p2, p3, p4), ('pieces','instant','grains','grinded'), loc="right")

pyplot.ylim(0, 1.05)
pyplot.xlim(0, 21)

pyplot.grid()

pyplot.savefig('coop_coffee.png')
