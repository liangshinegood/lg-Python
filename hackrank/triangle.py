# 思路在于：1的时候循环一次，二的时候循环两次�
# 每一次循环在一行打印(1.整型位的思路；2.字符重复思路)

for i in range(1,int(input())):
#    print("%d"%i)*i
    print((10**(i)//9)*i)
    print("".join([str(i)]*i))


