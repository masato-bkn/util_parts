# リスト-> 辞書へ作成
def convertToDict(data):

    dictionary = {}

    for d in data:
        dictionary[d[0]] = d[1]
    
    return dictionary

data = [["バナナ",10],["りんご",5],["ぶどう",12]]

print(convertToDict(data))
