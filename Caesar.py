
#シーザー暗号化
def caesar_cipher(word ,key):
    sentence=""
    
    #全ての文字について数に変更し処理を行う
    for i in word:
        Before=ord(i)+int(key)
        
        #ここでは制御文字計１２７個を対象としている
        After=Before%127
        sentence+=chr(after)
        
    return sentence

#シーザー暗号解読
def caesar_solve(word):
    for n in range(0,126):
        sentence=""
        for i in word:
            
            Before=ord(i)-n
            After=Before%126
            sentence+=chr(After)
        
        print(sentence)





    