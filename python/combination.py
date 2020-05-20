# リスト-> 辞書へ作成
# def convertToDict(data):

#     dictionary = {}

#     for d in data:
#         dictionary[d[0]] = d[1]
    
#     return dictionary

# data = [["バナナ",10],["りんご",5],["ぶどう",12]]

# print(convertToDict(data))


# 3
# 10
# 5  400
# 7  1000
# 3  350

import itertools as it

n = int(input())
w = int(input())
items = [list(map(int,input().split())) for i in range(3)]

# 商品の重さと値段の辞書を作成する。
item_dict = {}
for item in items:
    item_dict[item[0]] = item[1]

# 商品の重さの組み合わせを作成する。
comb = []
for i in range(1,n+1):
    comb.extend(list(it.permutations([item[0] for item in items],i)))
print(comb)


# そのうち、重さの合計がw以下になるものを配列に詰める。
tmp = []
for c in comb:
    if sum(c) <= w:
        tmp.append(c)

# 配列をソートして先頭にあるものを取得
# 商品の値段を辞書から引っ張り出して、合計金額を算出する。
ans = 0
for t in sorted(tmp,reverse=True)[0]:
    ans += item_dict[t]
print(ans)
