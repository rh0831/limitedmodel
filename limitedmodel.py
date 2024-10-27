import random

g = 100000 #ゲームの実施回数
n = 10 #カードの枚数
m = 1 #再抽選の回数
p = 3 #プレイヤー人数
score = 0 #合計点
countlist = [] #出現回数カウント用リスト

for i in range(0,n+1):
    countlist.append(0)

for i in range(0,g):
    card = 0 #手持ちのカード
    temp = 0 #比較対象のカード
    list = [] #カードのリスト
    re = m + 1 #残り再抽選回数 初回分を考慮して１加算
    rep = p #残りプレイヤー数

    for j in range(0,n):
        list.append(j+1)
    random.shuffle(list)

    for j in range(0,n):
        if ( list[j] > temp ):
            temp = list[j]
            re -= 1
            if( re < 1 and random.random() < 1.0/rep) : #もう再抽選を行わない場合に、残りプレイヤーでジャンケンする
                card = list[j]
                break
            elif (re < 1): #じゃんけんに負けた場合は、プレイヤー数を１減らす
                rep -= 1 
    score += card #残ったカードをスコアに加算
    countlist[card] = countlist[card] + 1 #出現回数を加算

print("平均点") 
print(score / g)
print(countlist)
