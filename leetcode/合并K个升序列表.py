class Solution:
    # 分治（递归）类似归并排序
    # 两两之间归并排序
    def mergeKLists(self, lists):
        # 主函数
        if not lists:
            return
        n = len(lists)
        left=0
        right=n-1
        if left==right:
            return lists[left]
        mid=left+(right-left)//2
        l=self.mergeKLists(lists[:mid+1])
        r=self.mergeKLists(lists[mid+1:])
        return self.mergeLists(l,r)

    def mergeLists(self, l1, l2):
        # 合并两个lists
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeLists(l1, l2.next)
            return l2
