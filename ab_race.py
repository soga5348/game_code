from random import randint
from time import sleep
 
a=0
b=0
goal=50
 
print("aとbどちらが先にゴールするかを当てるゲーム")
you=input("どちらを選びますか？(同時ならc):")
print("競争開始")
 
while a<=goal and b<=goal:
    a+=a+randint(0,3)
    b+=b+randint(0,3)
    print("A:"+">"*a+"@")
    print("B:"+">"*b+"@")
    sleep(1)

print("----------------------")

sleep(2)
 
if a>b:
    winner="a"
if a<b:
    winner="b"
if a==b:
    winner="c"
 
if winner==you:
    print("勝利")
else:
    print("敗北者じゃけぇ！！")