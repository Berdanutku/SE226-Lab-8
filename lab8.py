from abc import ABC

class a(ABC):
    def __init__(self,address):
        self.address=address

    def calculateFreqs(self,address):
        pass

class ListCount(a):
    def __init__(self, address):
        a.__init__(self, address)

    def calculateFreqs(self,address):
        list=[]
        list2=[]
        file=open(address)
        read=file.readline().split()
        for x in read:
         for y in x:
            if y not in list:
                list.append(y)
            else:
                list2.append(y)
        for x in range(0, len(list)):
            list.sort()
            tmp=list[x]
            print(list[x],"-",list2.count(tmp)+1)


class DictCount(a):
    def __init__(self, address):
        a.__init__(self, address)

    def calculateFreqs(self,address):
        dict={}
        file=open(address)
        read=file.readline().split()
        for x in read:
            for y in x:
             if (dict.__contains__(y)):
                tmp=dict[y]
                dict[y]=tmp+1
             else:
              dict[y]=0
        sortedDict=sorted(dict)
        for x in sortedDict:
            print(x,":",dict[x]+1)


address=r'C:\Users\berda\PycharmProjects\pythonProject\weirdWords.txt'

print("Resulting List")
list=ListCount(address)
list.calculateFreqs(address)
print("--------------------------")
print("Updated Dict")
dict=DictCount(address)
dict.calculateFreqs(address)