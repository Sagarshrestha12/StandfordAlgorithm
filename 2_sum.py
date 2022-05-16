x=[]
with open('test.txt') as file:
    for i in file:
        x.append(int(i));
# print(x)
def createHashTable(x):
    newDict ={};
    for i in range(len(x)):
        newDict[i]=x[i];
    return newDict;

def sum_2(hashTable,x):
    status = 0;
    for key,value in hashTable.items():
        sumT = value+x;
        if(value == x):
            continue;
        if(sumT>=-10000 and sumT<= 10000):
            status +=1;
    return status

def sumPair(x):
    hashT=createHashTable(x);
    newhash=createHashTable(x);
    count=0;
    # print(hashT)
    for key, value in hashT.items():
        count+=sum_2(newhash,value)
        newhash.pop(key);

    return count;

print(sumPair(x))