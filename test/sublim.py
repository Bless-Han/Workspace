'''
输入两个非负 10 进制整数 A 和 B (≤2 
30
 −1)，输出 A+B 的 D (1<D≤10)进制数。
输入格式：

输入在一行中依次给出 3 个整数 A、B 和 D。

输出格式：

输出 A+B 的 D 进制数。

输入样例：

123 456 8

输出样例：

1103

'''

a, b, d = map(int, input().split())
c = a + b
result = ''
while c != 0:
	result += str(c % d)
	c = c // d
print(result[::-1])

