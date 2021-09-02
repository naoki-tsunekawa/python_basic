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

# タプル型
# 値を入れたら後は"読み込み専用"の使い方をする場合に使う
# メソッドが.indexと.countくらいしかないから
# help(tuple)を確認するとわかる
t = (1, 2, 3, 4, 5, 1, 1)
print(type(t))
print(t)
# タプル型では以下のように再代入できない
# t[0] = 100
print(t[0])
print(t[1:4])
# index関数　要素の位置を検索する
print(t.index(1))
# 1の次の１の位置を検索する
print(t.index(1, 1))
# 要素の個数
print(t.count(1))

# タプル内にリストを入れる事ができる
t = ([1, 2, 3], [4, 5, 6])
print(t)
# タプルの中のリストの要素は変更可能
t[0][0] = 7
print(t)

# 出力結果
# ([1, 2, 3], [4, 5, 6])
# ([7, 2, 3], [4, 5, 6])

# カッコをつけなくてもカンマを入れた時点でタプルになる
t2 = 1,
print(type(t2))
# 出力結果
# <class 'tuple'>

# 空のタプルを宣言した後に1を代入するとint型になってしまうので注意
t = ()
print(type(t))
t = (1)
print(type(t))
# 出力結果
# <class 'tuple'>
# <class 'int'>
# 文字列でも同様

# タプルの連結
new_tuple = (1, 2, 3) + (4, 5,)
print(new_tuple)
# 出力結果
# (1, 2, 3, 4, 5)

# タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)
# 出力結果
# (10, 20)

x, y = num_tuple
print(x, y)
# 出力結果
# 10 20
# xとyにそれぞれを代入している
# x, y = 10, 20
# pythonではx, yにそれぞれtupleを展開するという意味になる
# 例えば...
min, max = 0, 100
print(min, max)
# ※ただ長すぎるとコードが読み辛くなるので注意

# iとjの値を入れ替えたい
i = 10
j = 20

i, j = j, i
print(i, j)
