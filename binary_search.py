size = 10
a = [1,2,3,4,4,5,6,7,8,9]
b = 10
def binary_search(a,b):
    start = 0
    end    = 9

    while(start<=end):
        mid = (start+end) //2
        if b == a[mid]:
            print(f'{b} is in the {mid } position ')
            return 
        elif b > a[mid]:
            start = mid+1
        else:
            end = mid
    print(f'{b} is not in the array')


if __name__== "__main__":
    binary_search(a,b)
    binary_search(a,1)
    binary_search(a,11)