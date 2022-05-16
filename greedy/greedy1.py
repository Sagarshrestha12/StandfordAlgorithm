import math
from random import random

def deepcopy(arr):
    newArr=[];
    for i in range(len(arr)):
        newArr.append(arr[i]);
    return newArr;

# import copy
x=[3,4,5,1,2,6,10]
y=deepcopy(x)
y.append(12)
# print(x,y,end='-')

def randomNumber(mini, maxi):
    return math.floor(random()*(maxi-mini+1)) +mini;

def shuffle(arr):
    newarr=deepcopy(arr);
    for i in range(len(arr)):
        i1=randomNumber(0,len(arr)-1);
        j1=randomNumber(0,len(arr)-1);
        newarr[i1],newarr[j1]=newarr[j1],newarr[i1];
    return newarr
# # x=[[i,i+1, i+2] for i in range(10)]
# print(shuffle(k))
# print(k)

def partition(arr,pivot,ind):
    l=len(arr)
    shuffled_arr =shuffle(arr);
    i=0;
    for j in range(l):
        if(shuffled_arr[j][ind]>pivot):
            shuffled_arr[j],shuffled_arr[i]=shuffled_arr[i],shuffled_arr[j];
            i+=1;
    return i;

def sortByWeight(scheduledJob,ind,pivot):
    if(ind==len(scheduledJob)-1):
        return
    j=ind+1
    while(j<=len(scheduledJob)-1 and scheduledJob[j][2]==pivot):
        k=j-1;
        weight=scheduledJob[j][0]
        while(k>=ind and weight > scheduledJob[k][0] ):
            scheduledJob[k+1],scheduledJob[k]=scheduledJob[k],scheduledJob[k+1];
            k-=1;
        j+=1;
# arr=[[1,2],[18,22],[12,10],[10,10],[8,10],[1,40]]
# sortByWeight(arr,2,10);


# print(arr)
scheduledJob=[]
p=[]
with open('./greedy/input/jobs.txt') as file:
    lines =file.readlines()
    n=int(lines[0].strip());
    # old_list=lines[1].strip().split();
    # new=[int(i) for i in old_list]
    # pivot=new[0]-new[1];
    # new.append(pivot);
    # scheduledJob.append(new)
    for i in range(1,n+1):
        old_list=lines[i].strip().split();
        new=[int(i) for i in old_list]
        pivot=new[0]/new[1];
        new.append(pivot);
        ind =partition(scheduledJob,pivot,2);
        scheduledJob.insert(ind,new)
        sortByWeight(scheduledJob,ind,pivot);
# print(scheduledJob)

def weighted_completion(arr):
    weighted_sum =0;
    completion_time = 0;
    for i in range(len(scheduledJob)):
        completion_time += scheduledJob[i][1];
        weighted_sum=weighted_sum + ( scheduledJob[i][0]*completion_time);
    return weighted_sum;

# print(len(scheduledJob))
print(weighted_completion(scheduledJob))
# pivot =17;
# arr=[1,4,9,15]
# ind = partition(arr,pivot)
# arr.insert(ind,pivot)
# print(arr)

# num=7
# i=0;
# binary_res= 0;
# while(num!=0):
#     rem = num%2;
#     binary_res= rem*(10**i) + binary_res;
#     num= num//2;
#     i+=1;
# print(binary_res)



# inpt = "ab"
# i=[1,2]
# sequen ="abcdabababd";
# count=0;
# for i in range(len(sequen)):
#     if(sequen[i:i+len(inpt)]==inpt):
#         count+=1;

# print(count)

# def change(i):
#     for k in range(len(i)):
#         i[k]*=2;
# l=i;

# change(i)
# print(i,l)
# x=[1,2]
# print(len(x))

def insertion(arr):
    j=1;
    for i in range(1,len(arr)):
        pivot= arr[i]
        k=i-1;
        while(k>=0 and pivot<arr[k]):
            arr[k],arr[k+1]=arr[k+1],arr[k];
            k-=1
    return arr

# arr=[2,4,1,9,1,7,12,50,35]
# print(insertion(arr))