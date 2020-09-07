class Trie:
    # apple:{'a': {'p': {'p': {'l': {'e': {'end': True}}}}}}             #第一次insert，最后一个'e'存在结束'end'
    # app:  {'a': {'p': {'p': {'l': {'e': {'end': True}}, 'end': True}}}}#第二次insert，第二个'p'存在结束'end'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        train = self.dict
        for alpha in word:
            if alpha not in train:
                train[alpha] = {}
            train = train[alpha]
        train["end"] = "True"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        test = self.dict
        for alpha in word:
            if alpha not in test:
                return False
            test = test[alpha]
        if "end" in test:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        test = self.dict
        for alpha in prefix:
            if alpha not in test:
                return False
            test = test[alpha]
        return True