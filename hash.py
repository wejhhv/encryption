from hashlib import md5
from minbc_lib.hash import*

#バイナリ―データでないとハッシュ関数に適用できない
num=bytes(5152)

#ハッシュ化
hashed=md5(num).hexdigest()
#5152→0d912f3f39fb2811ac01d4d9a8bfcef0

#ハッシュ値より元の数字を求める
str="0d912f3f39fb2811ac01d4d9a8bfcef0"





for key in range(0,10000):
    
    if md5(bytes(key)).hexdigest()==str:
        
        print(key)
        break


