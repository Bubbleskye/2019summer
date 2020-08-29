class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2)>len(str1):
            str1,str2=str2,str1
        i=0
        j=0
        res=""
        while i < len(str2) and j < len(str1):
            if str2[i]!=str1[j]:
                return ""
            res=res+str2[i]
            i=i+1
            j=j+1
        while j+len(res)<=len(str1):
            if str1[j:j+len(res)]==res:
                j=j+len(res)
            else:
                break
        if j==len(str1):
            return res
        else:
            return self.gcdOfStrings(str1[j:], res)
solution=Solution()
str1="ABABAB"
str2="ABAB"
res=solution.gcdOfStrings(str1,str2)
print(res)