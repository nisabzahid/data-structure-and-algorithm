s = {}
for _ in range(int(input())): r = input(); print(r+str(s[r]) if s.setdefault(r,0) else "OK") ; s[r] += 1
   
