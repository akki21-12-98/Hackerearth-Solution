N = int(input())
lst = list(map(int,input().split()))
s = sum(lst)
minn = min(lst)
maxx = max(lst)
print(s-maxx,s-minn)
