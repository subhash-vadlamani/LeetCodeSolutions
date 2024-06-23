from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj_list = defaultdict(list)
        word_len = len(beginWord)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        

        while queue:
            current_word, level = queue.popleft()

            if current_word in visited:
                continue

            if current_word == endWord:
                return level
            
            visited.add(current_word)

            for i in range(word_len):
                pattern = current_word[:i] + '*' + current_word[i+1:]

                for newWord in adj_list[pattern]:
                    queue.append((newWord, level + 1))
        return 0
        