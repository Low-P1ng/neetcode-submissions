class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        q = deque()
        q.append(beginWord)
        words=set(wordList)

        def check(this, that):
            check = 0
            for i in range(len(this)):
                if this[i]!=that[i]:
                    check+=1
                if check>1:
                    return False
            return check == 1

        while q:
            for i in range(len(q)):
                this = q.popleft()
                for word in list(words):
                    if check(this, word):
                        if word == endWord:
                            return res+1
                        q.append(word)
                        words.remove(word)
                print(res, q)
            res += 1

        return 0
