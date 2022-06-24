"""
https://leetcode.com/discuss/interview-question/810154/binary-autocomplete

https://www.geeksforgeeks.org/trie-insert-and-search/

https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
"""


""" 
Binary auto-complete using Trie. 

Given a sequence of commands entered into the console, for each command, determine the index of the command
last displayed, where we display the previously entered command that has the longest suffix. 
Return 0 if there is none.

Example: n = 6
command = ['000', '1110', '01', '001', '110', '11']

1. '000' - 0 (no command previously entered)
2. '1110' - 1 (no previous command shares a common prefix, so the last command is shown)
3. '01' - 1 ('000' shares the prefix '0' with the first command)
4. '001' - 1 (shares the prefix '00' with the first command)
5. '110' - 2 ('110' shares prefix '11' with the second command)
"""


class TrieNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None


"""		
example of commands ['000', '1110', '01', '001', '110', '11'] will look like this:
	  		  root
			/      \
	     '0'        '1'
	     /\           \
        / '1'          '1'        
	  '0'              / \     				
      /  \           '0'   \ 
     /	 '1'			   '1'
   '0'					   /
   						 '0'	
"""


def insert(root, string, idx):
    current_node = root
    output = idx

    for char in string:
        if current_node.left and char == current_node.left.val:
            current_node = current_node.left
            output = current_node.index + 1
            current_node.index = idx
        elif current_node.right and char == current_node.right.val:
            current_node = current_node.right
            output = current_node.index + 1
            current_node.index = idx
        else:
            new_node = TrieNode(char, idx)
            if char == '0':
                current_node.left = new_node
                current_node = current_node.left
            elif char == '1':
                current_node.right = new_node
                current_node = current_node.right
    return output


def auto_complete_binary(commands):
    output = []
    root = TrieNode('*', 0)
    for idx, command in enumerate(commands):
        index = insert(root, command, idx)
        output.append(index)
    return output


""" General Trie structure """


class TrieNodeGeneral:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26  # used for O(1) lookup: use arrays[length of alphabet]

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class TrieGeneral:

    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNodeGeneral()

    def _char_to_index(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.get_node()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord


# driver function
def general_trie():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = TrieGeneral()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    # shows how general Trie works
    general_trie()

    # shows how you can apply it to the binary auto-completion problem
    commands = ['000', '1110', '01', '001', '110', '11']  # ['100110', '1001', '1001111']
    indices_command_displayed = auto_complete_binary(commands=commands)
    print(indices_command_displayed)
