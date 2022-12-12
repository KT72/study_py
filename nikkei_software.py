#繰り返し

#範囲を検索する繰り返し
datas = [1,2,3]

for data in datas:
    print(data)

#機械的に範囲を提供する

for num in range(10):#10個の範囲　０～９：ゼロスタート
    print(num)

#データ（値）：属性　　メソッド（処理）：振舞
fruits = ["みかん","リンゴ","バナナ","桃"]
fruits_taruts = [elm + "タルト" for elm in fruits]
print(fruits_taruts)
