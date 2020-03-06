def quicksort(array):
    if(len(array)<2):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for  i in array[1:] if i >pivot]
        return quicksort(less)+ [pivot] + quicksort(greater)
   
if __name__ == "__main__":
    print (quicksort([0,1,3,41,5,1,5,6]))