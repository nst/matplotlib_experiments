#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot
import numpy
import re

data = numpy.recfromcsv('coop_coffee.csv', delimiter='\t')

cat_names = ('misc', 'pieces', 'instant', 'grains', 'grinded')
categories = dict((name, []) for name in cat_names)

categories['pieces'] = [row for row in data if re.search("pièces|portions|sachet|capsule|nescafé dolce gusto", row[2], re.IGNORECASE)]
categories['instant'] = [row for row in data if re.search("soluble|instant", row[2], re.IGNORECASE)]
categories['grains'] = [row for row in data if re.search("grains", row[2], re.IGNORECASE)]
categories['grinded'] = [row for row in data if re.search("moulu", row[2], re.IGNORECASE)]
categories['misc'] = set(data) - set(sum(categories.values(), []))

pyplot.gca().set_color_cycle(['lightGray', 'red', 'blue', 'green', 'yellow'])

for name in cat_names:
    rows = categories[name]
    x = [r[0] for r in rows]
    y = [r[1] for r in rows]
    
    label = "%s (%d)" % (name, len(rows))
    pyplot.plot(x, y, marker='o', alpha=0.75, linestyle='none', label=label)

pyplot.title("Coffee, Coop, July 2012")
pyplot.xlabel("Price [CHF]")
pyplot.ylabel("Weight [Kg]")
pyplot.ylim(0, 1.05)
pyplot.xlim(0, 21)
pyplot.grid()
pyplot.legend(numpoints=1, loc="right")

pyplot.savefig('coop_coffee.png')
