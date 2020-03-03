# disjoint set is storing all data in distinct sets where only the sets are related
# creating a set of 5 element disjoint set
# every set will have one distinct representative

element = 5

par = [None]*(element+1)# creation of element size array

# at first all the elements are parent of their own

def makeset(n):
    par[n] = n
for i in range(1,element+1):
    makeset(i)

# all the element have their own representative
# now we have to make a funtion that will return if two nodes or elements are already friend
def union(a,b):
    u = find(a)
    v = find(b)
    if u==v :
        print("they are already friend") 
    else 
        par[u] = v #or par[v] = u


def find(r):
    if par[r]==r:
        return r
    return find(par[r])



if __name__ == "__main__":
    pass
    