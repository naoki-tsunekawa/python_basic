# Dictionary(辞書型)
# カーリーブラケット {}
d = {'x': 10, 'y': 20}
print(type(d))
print(d['x'])
print(d['y'])
d['z'] = 200
print(d)
# 出力結果
# {'x': 10, 'y': 20, 'z': 200}

d[1] = 100000
print(d)
# 出力結果
# {'x': 10, 'y': 20, 'z': 200, 1: 100000}

# Dictの生成の仕方
dict1 = dict(a=10, b=20)
print(dict1)
# 出力結果
# {'a': 10, 'b': 20}

dict2 = dict([('a', 10), ('b', 20)])
print(dict2)
# 出力結果
# {'a': 10, 'b': 20}

# dictのメソッド(代表的なもの)
# keys()とvalues()
d = {'x': 10, 'y': 20}
print(d.keys())
print(d.values())
# 出力結果
# dict_keys(['x', 'y'])
# dict_values([10, 20])

# dictの更新メソッド
# update()　上書きする（オーバーライドする）
d2 = {'x':  1000, 'j': 500}
d.update(d2)
print(d)
# 出力結果
# {'x': 1000, 'y': 20, 'j': 500}

# dictの中身をとる
print(d['x'])
print(d.get('x'))
# 出力結果
# 1000
# 1000
# キーがないものはエラー
# getメソッドを使った場合は Noneを返す

# dictの中身を取り出したい
# pop()
print(d.pop('x'))
# 出力結果
# 1000

# dictの中身を削除したい
# del
print(d)
# 出力結果
# {'y': 20, 'j': 500}
del d
# print(d)
# 出力結果
# NameError: name 'd' is not defined

d = {'x': 100, 'y': 200}
# clear　初期化
d.clear()
print(d)
# 出力結果
# {}

# dictの中のキーを指定して検索するメソッド
d = {'x': 100, 'y': 200}
# 'x' in d
print('x' in d)
# 出力結果
# True

# 辞書のコピー
# リストの時同様参照渡しに注意
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)
# 出力結果
# {'a': 1000}
# {'a': 1000}

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
# 出力結果
# {'a': 1}
# {'a': 1000}

# 辞書の使い所
fruits = {
	'apple': 100,
	'banana': 200,
	'orange': 300,
}

# appleの値段を取り出したい
print(fruits['apple'])
# リストでは簡単に見つけにいけない。
# 例えば人の名前で年齢をとってきたい時など辞書を使う方が便利
# リスト型で検索する場合は処理が遅くなる
# 辞書型で検索する際はハッシュテーブルを持っているので、
# キーがわかれば高速に検索できる
# 例えるなら本の目次みたいなもの
