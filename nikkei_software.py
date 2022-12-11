#組み込み関数　インポートせずに利用可能な関数
data = [1,2,3,4]
print(len(data)) #print関数とlen関数

#ライブラリ関数の活用

#ライブラリ関数の集まりモジュールの呼び出しと利用例
import random
print(random.randint(1,6))

#モジュールに別名をつけて利用例
import random as r
print(r.randint(1,6))

#モジュールからライブラリ関数を取り出して利用例
from random import randint
print(randint(1,10))
