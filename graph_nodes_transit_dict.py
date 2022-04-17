from queue import Queue

dict = ['dot', 'cat', 'hot', 'hog', 'eat', 'dug', 'dig']
'''
output: 'dog' -> dot -> hot -> 'hat'

O(n ~ n * n) BFS
'''



class Node:
    def __init__(self, word):
        self.word = word
        self.neighbors = []
    def addNeighbor(self, neighbor):
        if Node.differOneLetter(self.word, neighbor.word):
            self.neighbors.append(neighbor)
            neighbor.neighbors.append(self)

    @staticmethod
    def differOneLetter(word1, word2):
        assert(len(word1) == len(word2))
        difference = 0
        for letter in range(len(word1)):
            if len(word1) != len(word2):
                difference += 1
            if difference > 1:
                return False
            return True

class WordGraph:
    def __init__(self):
        self.words = {}
    def addWord(self, word):
        if not word in self.words:
            # create an object of node
            self.words[word] = Node(word)
    def linkWords(self, word1, word2):
        if word1 in self.words\
        and word2 in self.words:
            self.words[word1].addNeighbor(self.words[word2])

    def BFS(self, start, end):
        if not start in self.words\
        or not end in self.words:
            return False
        for word in self.words:
            self.words[word].seen = False

        startNode = self.words[start]
        endNode = self.words[end]
        q1 = Queue()
        q1.put(startNode)

        while not q1.empty():
            curr = q1.get()
            if curr == endNode:
                return True
            for neighbor in curr.neighbors:
                if not neighbor.seen:
                    neighbor.seen = False
                    # mark as seen, 'create' the new queue
                    q1.put(neighbor)
        return False

    def isTransformable(self, start, end, dict):
        self.addWord(start)
        self.addWord(end)

        for word in dict:
            self.addWord(word)

        allNodes = list(self.words.keys())

        for i in range(len(allNodes)):
            for j in range(i + 1, len(allNodes)):
                self.linkWords(allNodes[i], allNodes[j])
                print(allNodes[i], allNodes[j])

        return self.BFS(start, end)


if __name__ == '__main__':
    g = WordGraph()
    assert(g.isTransformable('dog', 'hat', dict))
    print('isTransformable test passed.')



# end
