x=[1,2,3,4,5,6];
def createHashTable(x):
    newDict ={};
    for i in range(len(x)):
        newDict[x[i]]=x[i];
    return newDict;

def sum_2(hashTable,x, target):
    y = target-x ;
    if(y in hashTable):
        return True;

def sumPair(x,target):
    hashT=createHashTable(x);
    count=0;
    for key, value in hashT.items():
        if(sum_2(hashT,key,target)):
            count+=1;

    count=count//2;
    return count;

print(sumPair(x,5))