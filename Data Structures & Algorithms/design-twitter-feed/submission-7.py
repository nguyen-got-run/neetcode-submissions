class User:
    def __init__(self, uid: int):
        self.uid = uid
        self.tweets = deque()
        self.follows = {}
    
    def tweet(self, tweetId: int, globalCounter: int):
        self.tweets.append((globalCounter, tweetId))
        if len(self.tweets) > 10:
            self.tweets.popleft()

    def getUid(self): return self.uid
    def getTweets(self): return self.tweets
    
    def getNewsFeed(self):
        ans = []
        for tid in self.tweets:
            ans.append(tid)
        
        for uid in self.follows:
            user = self.follows[uid]
            tweets = user.getTweets()
            for e in tweets: ans.append(e)
        
        heapq.heapify(ans)

        ans = heapq.nlargest(10, ans)
        return list(map(lambda e: e[1], ans))

    
    def follow(self, followee: User):
        self.follows[followee.getUid()] = followee
    
    def unfollow(self, followeeId: int):
        if followeeId in self.follows:
            del self.follows[followeeId]

class Twitter:
    def __init__(self):
        self.userMap = {}
        self.globalCounter = 0
    
    def getUserById(self, userId: int) -> User:
        if userId in self.userMap: user = self.userMap[userId]
        else: self.userMap[userId] = User(userId)

        return self.userMap[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUserById(userId)

        self.globalCounter += 1
        user.tweet(tweetId, self.globalCounter)

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getUserById(userId)
        return self.userMap[userId].getNewsFeed()

    def follow(self, followerId: int, followeeId: int) -> None:
        user = self.getUserById(followerId)
        followee = self.getUserById(followeeId)
        user.follow(followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.getUserById(followerId)
        user.unfollow(followeeId)
        
