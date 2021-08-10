# 変数宣言
# 型宣言をしなくても良い
# 変数名の先頭に数字を入れることはできない　2num ×
num = 1
name = 'Mike'
is_ok = True

print(num)
print(name)

# 型確認は type()で調べる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 変数に違う型を代入することが出来る
num = name
print(num, type(num))

# print
# つなげて記述するとスペースでつなげて出力される
print('hi', 'Mike')
# sep=''で指定するとスペースの代わりに入るものを指定できる
# separateの略
print('hi', 'Mike', sep="!")
# end
print('hi', 'Mike', sep="!", end='.\n')

# 文字列
print('I don\'t know')
print("I don't know")

# 改行
print('hello. \nHow are you?')
# path
print(r'c:\name\name')

print("""\
line1
line2
line3\
""")

print('Hi.' * 3 + 'Mike.')

word = 'python'
print(word[0])
print(word[1])
print(word[-1]) # 最後の文字出力
# スライス
print(word[0:2])
print(word[:2])
print(word[2:])

word = 'j' + word[1:]
print(word[:])
# 文字列の長さ
n = len(word)
print(n)

# 文字列のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)

# この文字列で始まっているか？
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

# 前から検索
print(s.find('Mike'))
# 後ろ（のもの）から検索
print(s.rfind('Mike'))

print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

# 文字の代入
print('a is {} {} {}'.format(1, 2, 3) )

print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='naoki', family='tsunekawa'))

# str()で型を変換できる
x = str(1)
print(type(x))
