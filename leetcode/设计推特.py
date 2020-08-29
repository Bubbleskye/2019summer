# defaultdict()在dict()的基础上添加了一个missing(key)的方法
# 在调用一个不存在的key的时候，defaultdict函数会调用“missing”，返回一个int,set,list,dict对应的默认数值，不会出现keyerror的情况。
from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeline = defaultdict(list)
        # 定义一个字典，里面的元素是列表，存储一个用户发的微博
        self.userId_follower = defaultdict(set)
        # 定义一个字典，里面的元素是集合，存储一个用户关注的人
        self.now = 0
    #     时间

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timeline[userId].append((self.now, tweetId))
        # 以用户ID为key，时间+推特id为value
        self.now += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # 输入查看人的userid
        # self.userId_follower[userId] 中存储的是userId关注的人 通过|操作，得到并集，也就是加上了userid本人
        res = []
        for uid in self.userId_follower[userId] | {userId}:
            for tmp in self.timeline[uid]:
                res.append(tmp)
        #         将关注的人以及本人发的所有微博放到列表中
        res.sort(reverse=True)
        # reverse=True 降序排列,自动按照set的第一个元素降序排序
        return [tw for _, tw in res[:10]]
    # 前10条即为新的十条微博

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.userId_follower[followerId].add(followeeId)
    # add向集合中加入元素
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """

        self.userId_follower[followerId].discard(followeeId)
# discard移除集合中的元素