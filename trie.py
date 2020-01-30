#https://leetcode.com/problems/implement-trie-prefix-tree/
import collections
import pytest

class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def delete(self, word):
        """
        Returns True if the word is in the trie. False if the word doesn't exist
        :type word: str
        :rtype: bool
        """

        # check existence of the word first
        if not self.search(word):
            return False
        stack = list()
        current = self.root

        #traverse all the way down and stack up the map
        for w in word:
            stack.append(current.children)
            current = current.children.get(w)
        
        ch = stack.pop()
        ch[word[-1:]].isword = False            

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True

    trie.insert("app")   
    assert trie.search("app") == True

    assert trie.delete("ap") == False
    assert trie.delete("app") == True
    assert trie.search("app") == False

    assert trie.delete("apple") == True
    assert trie.search("apple") == False

    trie.insert("apple")
    assert trie.search("apple") == True




