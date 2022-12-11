#1行コードの実行
print("こんにちは")

#変数
num = 100
print(num)

#演算
num = num + 10
print(num)
num *= 50
print(num)

#リスト
week = ['月','火','水','木','金','土','日',]
print(week)
print(week[2])
print(week[1:4])
week[0],week[6] = week[6],week[0]
print(week)

#タプル
week = ('月','火','水','木','金','土','日',)
print(week)
print(week[2:7])
# week[0],week[6] = week[6],week[0] ERROR:書き換え不可

#辞書
week = {'mo':'月','tu':'火','we':'水','tu':'木','fr':'金','sa':'土','su':'日',}
print(week['tu'])