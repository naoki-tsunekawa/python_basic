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

# Listの操作
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'X'
print(s)
# Listの中身を変更する
s[2:5] = ['C', 'D', 'E']
print(s)
# Listの中身を削除する
s[2:5] = []
print(s)
s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8]
# Listの最後に追加する場合
n.append(100)
print(n)

# 所定の位置に挿入する
n.insert(1, 200)
print(n)

# 配列の中身を取り出す
print(n.pop())
print(n.pop(0))
print(n)

# 削除する
# delは強力なので、del n とした場合nの存在自体消えることになる
del n[0]
print(n)

n = [1, 2, 2, 2, 3, 4]
n.remove(2)

print(n)

# 結合
a = [1, 2, 3]
b = [6, 7, 8]
a += b
print(a)

x = [1, 2, 3]
y = [6, 7, 8]
x.extend(y)
print(x)

# Listのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3]
# indexメソッドを使えばリストの中の物の位置を検索できる
print(r.index(3, 3))

# カウント
print(r.count(3))

# ソート
r.sort()
print(r)

# 逆にソート
r.sort(reverse=True)
print(r)

# リストに分けて格納
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
# 元に戻す(文字列のメソッド)
x = ' '.join(to_split)
print(x)

#関数のヘルプの呼び出し
# print(help(list))


# リストのコピー x.copy() or x[:]
# 注意点
i = [1, 2, 3, 4, 5]
j = i #参照渡し
# ↑jを変更するとiも変わってしまう。

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

# リストの使い所
# バスの乗車人数判定
# ============================================
# バスの最大乗車人数が10人の場合
# 乗れるか乗れないかを判定する
# ============================================
seat = []
def BusRide(ride):
	max = 10
	min = 0
	if min <= len(seat) < max:
		seat.append(ride)
		print("OK")
	else:
		print("NG")

BusRide(1)
BusRide(2)
BusRide(3)
BusRide(4)
BusRide(5)
BusRide(6)
BusRide(7)
BusRide(8)
BusRide(9)
BusRide(10)
BusRide(11)
