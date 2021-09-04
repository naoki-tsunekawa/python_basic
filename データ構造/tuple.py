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

# タプルの使い所
# 選択肢の設問を投げて回答させるアプリケーション
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
