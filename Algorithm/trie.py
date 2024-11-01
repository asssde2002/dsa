class Node:
    def __init__(self):
      self.children = {}
      self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add_node(self, string):
        curr = self.root
        for s in string:
            if s not in curr.children:
                curr.children[s] = Node()

            curr = curr.children[s]

        curr.is_end = True

    def search_node(self, string):
        curr = self.root
        for s in string:
            if s not in curr.children:
                return False

            curr = curr.children[s]

        return curr.is_end


if __name__ == "__main__":
    string_list = ["apple", "apples", "you", "me"]
    trie = Trie()
    for string in string_list:
        trie.add_node(string)

    print("Check string (apple) exist: ", trie.search_node("apple"))
    print("Check string (you) exist: ", trie.search_node("you"))
    print("Check string (yo) exist: ", trie.search_node("yo"))



