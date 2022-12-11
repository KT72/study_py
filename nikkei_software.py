#自作関数の定義
from random import randint
def normal_dice():
    return randint(1,6)

#自作関数の呼び出し
print(normal_dice())

#規定値の活用
def multi_dice(eye = 6): #規定値6
    return randint(1,eye)

print(multi_dice(100))

#無名関数（ラムダ式）
dice = lambda eye=6:randint(1,eye)

print(dice(4))

