	class Solution(object):
		def checkIfExist(self, arr):
			cont=set()
			for i in range(len(arr)):
				if arr[i]*2 in cont or (arr[i]%2==0 and arr[i]//2 in cont):
					return True
				cont.add(arr[i])
			return False
