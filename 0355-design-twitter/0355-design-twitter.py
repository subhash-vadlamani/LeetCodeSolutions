from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.adj_list = defaultdict(list)
        self.i = 1
        # max heap to store the most recent tweets
        # self.heap = []
        self.tweets = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # push the tweet to the heap
        # heapq.heappush(self.heap, (-self.i, userId, tweetId))
        # self.i += 1

        self.tweets[userId].append((self.i, tweetId))
        self.i += 1
        
    # def is_follower(self,followeeId, followeeIdList):
    #     # if followeeId in self.adj_list[followerId]:
    #     #     return True
    #     # return False
        
    #     # followeeIdList is sorted
    #     l = 0
    #     h = len(followeeIdList) - 1
    #     while l <= h:
    #         m = (l + h) // 2

    #         if followeeIdList[m] == followeeId:
    #             return True
    #         elif followeeId < followeeIdList[m]:
    #             h = m - 1
    #         else:
    #             l = m + 1
    #     return False


    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId] + self.adj_list[userId]
        heap = []

        for user in users:
            if user in self.tweets:
                for tweet in self.tweets[user][-10:]:
                    heapq.heappush(heap, (-tweet[0], tweet[1]))
        
        news_feed = []
        while heap and len(news_feed) < 10:
            news_feed.append(heapq.heappop(heap)[1])
        return news_feed

        # popped_tweets = []
        # news_feed = []
        # count = 0
        # followeeList = sorted(self.adj_list[userId])

        # while self.heap and count < 10:
        #     current_popped_tweet = heapq.heappop(self.heap)
        #     popped_tweets.append(current_popped_tweet)
        #     if current_popped_tweet[1] == userId or self.is_follower(current_popped_tweet[1], followeeList):
        #         news_feed.append(current_popped_tweet[2])
        #         count += 1
        # for tweet in popped_tweets:
        #     heapq.heappush(self.heap, tweet)
        # return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.adj_list[followerId]:
            self.adj_list[followerId].append(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.adj_list[followerId]:
            self.adj_list[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)