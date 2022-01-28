5 lines (5 sloc)  112 Bytes
   
n=int(input())
score=map(int,input().split())
score=list(set(score))
score.remove(max(score))
print(max(score))
