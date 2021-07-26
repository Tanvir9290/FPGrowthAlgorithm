import numpy as np
import pandas as pd

class Node:
 
    # Function to initialise the node object
    def __init__(self, data,count='top'):
        self.data = data  # Assign data
        self.count = count
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
        

df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0, inplace=True)

transactions = []
for i in range(0,50):
    transactions.append([str(df.values[i,j]) for j in range(0,5) if str(df.values[i,j])!='0'])

minSup = int(input("Enter minimum support\n:- "))


def uniqueInd(mainArr):
    comArr = []
    for i in mainArr:
        for j in i:
            if j not in comArr:
                comArr.append(j)
    comArr = set(comArr)
    comArr = sorted(comArr)
    return list(comArr)

def oneCombMinCheck(checkArray):
    
    retArr = []
    dicto = {}
    for item in checkArray:
        dicto[item] = 0

        for transec in transactions:
            if item in transec:
                dicto[item] += 1
        
        if dicto[item] < minSup:
            del dicto[item]
    
    dicto = dict(sorted(dicto.items(), key=lambda item: item[1],reverse=True))
    for i,values in dicto.items():
        retArr.append(i)
    
    return retArr

def orderedTranList(getComb):
    retValue = []
    retIndex = []
    
    for trans in transactions:
        for comb in getComb:
            if comb in trans:
                retIndex.append(comb)
        if len(retIndex) != 0:    
            retValue.append(retIndex)
            
        retIndex = []
    
    return retValue


oneComb = uniqueInd(transactions)
oneComb = oneCombMinCheck(oneComb)
oneComb = orderedTranList(oneComb)


lList = LinkedList()
init = Node("top")

lList.head=init

for item in oneComb:
    temp = 0
    for specificItem in item:
        temp += 1
        if lList.head.next == None:
            tempNode = Node(specificItem,1)
            lList.head.next = tempNode
        elif temp == 1:
            if lList.head.data == specificItem:
                lList.head.count += 1
            else:
                
        elif temp > 1:
            
                
  

              




