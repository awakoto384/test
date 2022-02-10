# topass = [4,5,6]
# answered = [2,4,4]
# q = 3
# count = 0
# need = []
# for i in range(len(topass)):
#     need.append(topass[i]-answered[i])
# need.sort()
# print(need)
# while q>0 and len(need)>0:
#     temp = need.pop(0)
#     if q>=temp:
#         count+=1
#     q-=temp
# print(count)

# 前缀后缀相似性
# s = 'ababa'
# res = []
# for i in range(len(s)):
#     if s[i]!=s[0]:
#         res.append(0)
#     else:
#         count = 1
#         cur,ori = i,0
#         while cur+1<len(s) and s[cur]==s[ori]:
#             count+=1
#             cur+=1
#             ori+=1
#         res.append(count)
# print(res) 

# def getZarr(s, n, Z):
#     L, R, k = 0, 0, 0
     
#     for i in range(n):
#         if i > R:
#             L, R = i, i
#             while R < n and s[R - L] == s[R]:
#                 R += 1
#             Z[i] = R - L
#             R -= 1
#         else:
#             k = i - L
#             if Z[k] < R - i + 1:
#                 Z[i] = Z[k]
#             else:
#                 L = i
#                 while R < n and s[R - L] == s[R]:
#                     R += 1
#                 Z[i] = R - L
#                 R -= 1
                 
# def sumSimilarities(s, n):
#     Z = [0 for i in range(n)]
#     getZarr(s, n, Z)
#     total = n
#     for i in range(n):
#         total += Z[i]
#     return total

# s = "ababa"
# n = len(s)
# print(sumSimilarities(s, n))



# 字符串解码处理
# 字符转code
# s = 'acc'
# res = ''
# code = {'a':'1','b':'2','c':'3#'}
# point = 0
# while point<len(s):
#     res += code[s[point]]
#     count = 1
#     while point+1<len(s) and s[point+1]==s[point]:
#         count+=1
#         point+=1
#     if count!=1:
#         res = res+'('+str(count)+')'
#     point += 1
# print(res)
    


# 购物车账单
# products = [['10','d0','d1'],['15','EMPTY','EMPTY'],['20','d1','EMPTY']]
# discounts = [['d0','1','27'],['d1','2','5']]

# def find(products,discounts):
#     dis = {}
#     for i in discounts:
#         dis[i[0]]=[i[1],i[2]]
#     res = 0
#     for i in products:
#         temp = int(i[0])
#         for j in range(1,len(i)):
#             if i[j] in dis.keys():
#                 tp,d = dis[i[j]]
#                 if tp == "1":
#                     temp = min(temp,int(i[0])*(1-int(d)*0.01))
#                 elif tp=="2":
#                     temp = min(temp,int(i[0])-int(d))
#         res += temp
#         print(temp,'hi')
  
#     return res

# print(find(products,discounts))

# k个奇数
# def evenSubarray(lst, k):
#     res = set()
#     left, right, odd_num = 0, 0, 0
#     while right < len(lst):
#         if lst[right] % 2 == 1:
#             odd_num += 1

#         while odd_num > k and left < right:
#             if lst[left] % 2 == 1:
#                 odd_num -= 1
#             left += 1

#         for i in range(left, right + 1):
#             res.add(",".join(map(str, lst[i:right + 1])))

#         right += 1

#     return len(res)
# print(evenSubarray([2, 2, 5, 6, 9, 2, 11, 9, 2, 11, 12], 1))

