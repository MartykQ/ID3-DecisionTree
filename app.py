import model
from Builder import TreeBuilder
import os
import io



#################################################################
#                                                               #
#                                                               #
#          Zmien zmienna RESULT_NUMBER w module model           #
#                                                               #
#################################################################



##GRAPHVIZ PATH
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
## wymaga instalacji
##https://www.graphviz.org/download/



file = io.open('data.csv', 'r')  #BEZ POLSKICH ZNAKOW

simple = model.ModelTable()
simple.GetRawData(file)
simple.CleanRawData()

builder = TreeBuilder()
builder.Generate(simple)


builder.dot.render('output/round-table.gv', view=True)