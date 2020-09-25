class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
            if len(trust) == 0 and N==1:
                return 1
            trustcount = [0]*(N+1)
            for i in trust:
                trustcount[i[1]] += 1
        #print(trustcount[i[1]],i[1])
    
            for enum,i in enumerate(trustcount):
        #print( enum,i)
                if i == N-1:
            
                    for x in trust:
                        if enum == x[0]:
                            return -1           
                    return enum

            return -1
        
        
#print(Solution.findJudge(2,[[1,2]])) # return 2
#print(Solution.findJudge(1,[])) # return 1
#print(Solution.findJudge(3, [[1,3],[2,3]])) # return 3
 


        
