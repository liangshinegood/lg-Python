#思路：将setA,setB 输入的值到arry中进行判断如果有则加1然� -1

n,m = input().split()
arr = input().split()
setA = set(input().split())
setB = set(input().split())
print(sum([ (i in setA) - (i in setB) for i in arr]))
�
