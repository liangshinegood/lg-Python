# 思路：用set 方法中的intersection找出不同
# 将两种不同的值合并一下，最后答应闯隼�

a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b,key=int),sep='\n')


