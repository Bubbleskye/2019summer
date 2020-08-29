# s="aaaaa"
# res=[]
# tmp=""
# global count
# count=0
# def backtrack(s,tmp,res):
#     global count
#     if len(s)==0:
#         return res
#     for i in range(len(s)):
#         if i==0:
#             res.append(tmp+s[i])
#             test=tmp+s[i]
#             left=0
#             right=len(test)-1
#             while right-left>1:
#                 if test[left]!=test[right]:
#                     break
#                 else:
#                     left=left+1
#                     right=right-1
#             if right==left:
#                 count=count+1
#             if test[left]==test[right] and right-left==1:
#                 count=count+1
#         return backtrack(s[i+1:],tmp+s[i],res)
# for i in range(len(s)):
#     res.append(tmp+s[i])
#     count=count+1
#     backtrack(s[i+1:],tmp+s[i],res)
# print(count)
# print(res)
##超时

s="aaaaa"
count = len(s)
dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
for j in range(0, len(s)):
    for i in range(0, j):
        if (dp[i + 1][j - 1] != 0 or j - i < 3) and s[i] == s[j]:
            count = count + 1
            dp[i][j]=1
print(count)