class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):  # 正常插入前缀
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True  # 前缀结束时设为True

    def search(self, word):
        node = self
        res = ''
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:  # 没有子节点了，查找失败，直接返回原本的单词
                return word
            else:
                res += ch
                node = node.children[idx]
                if node.isEnd:  # 找到前缀，直接返回前缀
                    return res
        return word