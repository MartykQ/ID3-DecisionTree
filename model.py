import csv
import io
import math


RESULT_NUMBER = 5


class ModelTable:

    def __init__(self):
        self.raw_data = []
        self.data = [] #cleanData
        self.allEntropia = []
        self.results = []
        self.conditions = []
        self.label = ""
        self.answer = ""


    def GetRawData(self, plik):
        self.raw_data = list(csv.reader(plik, delimiter=';'))


    def CleanRawData(self):

        lastLine = []
        for i in range(0, len(self.raw_data[0])-1):
            lastLine.append('0')


        for i in range(0, len(self.raw_data)):
            self.conditions.append(self.raw_data[i][0])

        for i in range(len(self.raw_data)-RESULT_NUMBER, len(self.raw_data)):
            self.results.append(self.raw_data[i][0])

            for j in range(1, len(self.raw_data[i])):
                if self.raw_data[i][j] == '1':
                    lastLine[j-1] = self.raw_data[i][0]


        self.data = self.raw_data[:]

        for i in range(len(self.data)):
            del self.data[i][0]

        self.data = self.data[:-RESULT_NUMBER]

        self.data.append(lastLine)


    def PrintData(self):
        for line in self.data:
            print(line)


    def CalculateEntropiaRows(self):
        N = len(self.data[0])

        for i in range(0, len(self.data)-1): #-???

            enP = {} #przechowuje info ile roznych rezultatow bylo przy zalozeniu prawdziwosci jednego warunku
            enM = {} #przechowuje info ile roznych rezultatow bylo przy zalozeniu nieprawdziwosci jednego warunku

            for element in self.results:
                enP[element] = 0
                enM[element] = 0

            iPlus = 0
            iMinus = 0

            nPlus = self.data[i].count('1')
            nMinus = N - nPlus


            for j in range(0, N):
                if self.data[i][j] == '1':
                    enP[self.data[-1][j]] += 1

                elif self.data[i][j] == '0':
                    enM[self.data[-1][j]] += 1


            for key in enP:
                if enP[key] != 0:
                    iPlus = iPlus-(enP[key]/float(nPlus))*math.log((enP[key]/float(nPlus)), 2)


            for key in enM:
                if enM[key] != 0:
                    iMinus = iMinus-(enM[key] / float(nMinus)) * math.log((enM[key]/float(nMinus)), 2)

            entropia = (nPlus/float(N))*iPlus + (nMinus/float(N))*iMinus

            self.allEntropia.append(entropia)


    def DivideTable(self):
        """
        Dzieli tabele na 2 rozne tabele, wzgledem warunku z najmniejsza entropia. Gdy 2 lub wiecej warunkow ma taka sama
        entropie jako warunek przyjmuje pierwszy warunek z najmniejsza entropia.

        """

        self.CalculateEntropiaRows()
        N = len(self.data[0])

        pom = min(self.allEntropia)
        split_condition = 0

        """
        Problem w przypadku gdy entropia wszystkich warunkow jest taka sama
        """
        try:
            for i in range(0, len(self.allEntropia)):

                if self.allEntropia[i] == pom:
                    last_item = self.data[i][0]

                    for j in range(0, len(self.data[i])):
                        if self.data[i][j] != last_item:
                            split_condition = i
                            raise Exception
        except Exception:
            pass


        self.label = self.conditions[split_condition]

        new_array_one = []
        new_array_two = []

        for i in range(0, len(self.data)):
            new_array_one.append([])
            new_array_two.append([])

        for i in range(0, len(self.data)):
            for j in range(0, N):

                if self.data[split_condition][j] == '1':
                    new_array_one[i].append(self.data[i][j])

                elif self.data[split_condition][j] == '0':
                    new_array_two[i].append(self.data[i][j])

        """
        for line in new_array_one:
            print(line)


        for line in new_array_two:
            print(line)
        """

        returned_tables = []

        first_object = ModelTable()
        first_object.data = new_array_one
        first_object.results = self.results
        first_object.conditions = self.conditions
        returned_tables.append(first_object)

        second_object = ModelTable()
        second_object.data = new_array_two
        second_object.results = self.results
        second_object.conditions = self.conditions
        returned_tables.append(second_object)

        return returned_tables


    def IsDividable(self):

        if len(self.data[-1]) < 1:
            return False
        last_element = self.data[-1][0]

        for element in self.data[-1]:

            if element != last_element:
                return True

            else:
                last_element = element

        return False


    def GetAnswer(self):

        if not self.IsDividable():
            return self.data[-1][0]

        else:
            print("Tabela niepodzielna nie ma odpowiedzi")