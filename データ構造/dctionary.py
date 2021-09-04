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
