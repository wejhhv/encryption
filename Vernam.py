#バーナム暗号(鍵は平文以上の長さである必要がある)→復号も
def vernam_cipher(list,key):
    result=[]
    for p ,k in zip(list,key):
        result.append(p^k)
    return result



