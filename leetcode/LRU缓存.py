# 最近最少使用缓存 该缓存会删除最近最少使用的项目。使用之后就放到链表头部。
# 数据结构是:字典里面储存key对应的value是一个链表节点,链表节点中存有key,value,before,next,所以是一个双向链表
# dict[key]找到value,是一个链表节点.dict[key].key是节点中再次储存的key .value是值

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.before = None


class LRUCache:
    def __init__(self, capacity: int):
        from collections import defaultdict
        self.dict = defaultdict()
        self.capacity = capacity
        self.head = ListNode(-2, -2)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.before = self.head

    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1
        else:
            nownode = self.dict[key]
            benode = nownode.before
            afternode = nownode.next
            benode.next = afternode
            afternode.before = benode
            backnode = self.head.next
            nownode.next = backnode
            nownode.before = self.head
            self.head.next = nownode
            backnode.before = nownode
            return nownode.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            nownode = self.dict[key]
            nownode.val = value
            benode = nownode.before
            afternode = nownode.next
            benode.next = afternode
            afternode.before = benode
            backnode = self.head.next
            nownode.next = backnode
            nownode.before = self.head
            self.head.next = nownode
            backnode.before = nownode

        elif key not in self.dict.keys() and len(self.dict) == self.capacity:
            delnode = self.tail.before
            benode = delnode.before
            benode.next = self.tail
            self.tail.before = benode
            del self.dict[delnode.key]
            # 要记得删除字典中的key
            newnode = ListNode(key, value)
            self.dict[key] = newnode
            backnode = self.head.next
            newnode.next = backnode
            backnode.before = newnode
            newnode.before = self.head
            self.head.next = newnode

        else:
            backnode = self.head.next
            newnode = ListNode(key, value)
            self.dict[key] = newnode
            newnode.next = backnode
            newnode.before = self.head
            self.head.next = newnode
            backnode.before = newnode
