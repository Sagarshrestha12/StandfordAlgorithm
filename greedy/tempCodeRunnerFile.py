def shuffle(arr):
    newarr=deepcopy(arr);
    for i in range(len(arr)):
        i1=randomNumber(0,len(arr)-1);
        j1=randomNumber(0,len(arr)-1);
        newarr[i1],newarr[j1]=newarr[j1],newarr[i1];
    return newarr
