# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1
    # 定义全局变量的方式,定义到一个函数里面
    def Serialize(self, root):
        # write code here
        if not root:
            return "#!"
        res=""
        res=res+str(root.val)
        res=res+"!"+self.Serialize(root.left)+self.Serialize(root.right)
        return res
    def Deserialize(self, s):
        # write code here
        if s=="#!":
            return None
        arr = s.split('!')
        def DeserialCore(arr,index):
            self.flag=self.flag+1
            if index>len(arr):
                return None
            if arr[self.flag]!="#":
                root = TreeNode(int(arr[self.flag]))
                root.left = DeserialCore(arr,self.flag)
                root.right = DeserialCore(arr,self.flag)
                return root
            else:
                return None
        return DeserialCore(arr,self.flag)