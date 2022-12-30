# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.val = 1
        self.children = []

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return
        if word[-1] != "*":
            word += "*"
        needsToAdd = True
        for i in self.children:
            if word[0] == i.value:
                i.addWord(word[1:])
                needsToAdd = False
        if needsToAdd:
            newWord = WordDictionary()
            newWord.addWord(word[0])
            self.children.append(newWord)
            self.children[-1].addWord(word[1:])

    def search(self, word: str) -> bool:
        if word[-1] != "*":
            word += "*"
        found = False
        if word[0] == ".":
            for child in self.children:
                finding = child.search(word[1:])
                if finding == True:
                    return True
        else:
            for child in self.children:
                if child.val == word[0]:
                    finding = child.search(word[1:])
                    if finding == True:
                        return True
        return False


wordDictionary = WordDictionary();
print(wordDictionary.addWord("bad"))
print(wordDictionary.addWord("dad"))
print(wordDictionary.addWord("mad"))
print(wordDictionary.search("pad")) # return False
# print(wordDictionary.search("bad")) # return True
# print(wordDictionary.search(".ad")) # return True
# print(wordDictionary.search("b..")) # return True
