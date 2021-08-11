# Listの基本
l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[5])
print(l[0:3])
print(l[3:])

# 文字列をリストにいれる
print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2つ飛ばしで表示したい
print(n[::2])
# 後ろから
print(n[::-1])

# リストの中にリストをいれる
a = ['a', 'b', 'c']
n = [1, 2, 3]

x = [a, n]
print(x)

print(x[0][1])
print(x[1][2])
