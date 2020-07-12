import pandas as pd, numpy as np,os
import random

#Initial variables
n = 10
start = 0
stop = 99

#Define o vetor base utilizado os parâmetros dados do problema e a biblioteca random.choices
base_range = range(start,stop,1)

###Merge sort
merge_list = random.choices(base_range,k=n)

print ('\n\nMerge Sort')
print ('Lista original: ',merge_list)

#####
def merge_sort(merge_list): 
  
    if len(merge_list)>1: 
        m = len(merge_list)//2
        left = merge_list[:m]
        right = merge_list[m:]
        left = merge_sort(left)
        right = merge_sort(right)
  
        merge_list =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                merge_list.append(left[0]) 
                left.pop(0) 
            else: 
                merge_list.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            merge_list.append(i) 
        for i in right: 
            merge_list.append(i) 
    print (merge_list)
    return merge_list 


merge_list = merge_sort(merge_list)

print ('Lista ordenada por Merge Sort: ',merge_list)

##Bubble sort
bubble_list = random.choices(base_range,k=n)

print ('\n\nBubble Sort')
print ('Lista original: ',bubble_list)

def bubble_sort(bubble_list):
    length = len(bubble_list)
    for j in range(0,length-1):
        for i in range(0,length-j-1):  
            if bubble_list[i] > bubble_list[i+1]:
                temp_variable = bubble_list[i]
                bubble_list[i] = bubble_list[i+1]
                bubble_list[i+1] = temp_variable
    return (bubble_list)

bubble_list = bubble_sort(bubble_list)

print ('Lista ordenada por Bubble Sort: ',bubble_list)



