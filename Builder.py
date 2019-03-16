from graphviz import Digraph
import uuid
import model


class TreeBuilder:

    def __init__(self):
        self.dot = Digraph(comment='first')



    def Generate(self, table, PARENT="!START!", question = ""):

        id = str(uuid.uuid4())
        table.PrintData()

        if table.IsDividable():

            new_child = table.DivideTable()

            self.dot.node(id, label=table.label)
            self.dot.edge(PARENT, id, label=question)

            self.Generate(new_child[0], id, question='tak')
            self.Generate(new_child[1], id, question='nie')


        else:
            self.dot.node(id, label=table.GetAnswer())
            self.dot.edge(PARENT, id, label=question)
