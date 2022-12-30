# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        
    # Time and Space O(m) where m is the key length
    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        if word[-1] != "*":
            word += "*"
        needsToAdd = True
        for i in self.children:
            if word[0] == i.value:
                i.insert(word[1:])
                needsToAdd = False
        if needsToAdd:
            self.children.append(Trie(word[0]))
            self.children[-1].insert(word[1:])
        
    # O(m) time O(1) space (in ideal if we did iterative, here we did recursive so O(m))
    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True
        if len(word) != 0 and word[-1] != "*":
            word += "*"
        for i in self.children:
            if i.value == word[0]:
                return i.search(word[1:])
        return False
        
    # O(m) time O(h) space
    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        for i in self.children:
            if i.value == prefix[0]:
                return i.startsWith(prefix[1:])
        return False

trie = Trie()
trie.insert("apple")
# trie.insert("apple")
print(trie.search("apple"))
print(trie.search("ap"))
print(trie.startsWith("ap"))

        
