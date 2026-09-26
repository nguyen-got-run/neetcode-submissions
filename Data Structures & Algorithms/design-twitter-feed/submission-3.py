from datetime import datetime

class Twitter:

    def __init__(self):
        self.userTweetMap = {}
        self.userFollowMap = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        cur_time = self.counter
        self.counter -= 1
        
        if userId not in self.userTweetMap:
            self.userTweetMap[userId] = []
        
        self.userTweetMap[userId].append((cur_time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followingIds = set()
        followingIds.add(userId)

        if userId in self.userFollowMap:
            for followId in self.userFollowMap[userId]:
                followingIds.add(followId)
        
        maxHeap = []
        for uid in followingIds:
            if uid not in self.userTweetMap: continue 
            tweetItems = self.userTweetMap[uid]
            for tweetItem in tweetItems:
                maxHeap.append(tweetItem)

        heapq.heapify(maxHeap)

        ans = []
        while len(ans) < 10 and maxHeap:
            tweetTime, tid = heapq.heappop(maxHeap)
            ans.append(tid)
        
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowMap:
            self.userFollowMap[followerId] = set()
        
        self.userFollowMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowMap: return
        # print(str(self.userFollowMap[followerId]))
        self.userFollowMap[followerId].discard(followeeId)
