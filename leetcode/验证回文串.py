s="A man, a plan, a canal: Panama"
str=""
for c in s:
   if c.isalnum():
       # isalnum() 方法检测字符串是否由字母和数字组成
       str=str+c.lower()
#        str.lower()将字母转为小写
left=0
right=len(str)-1
while left<right:
    if str[left]!=str[right]:
        print(False)
    else:
        left=left+1
        right=right-1
print(True)


