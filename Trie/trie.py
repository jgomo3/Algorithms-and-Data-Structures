#!/usr/bin/env python3

class Trie:
    def __init__(self, words):
        self._root = {}
        for word in words:
            self._add_word(self._root, word)

    def _add_word(self, root, word):
        if word:
            descendent = root.setdefault(word[0], {})
            self._add_word(descendent, word[1:])

    def _contains(self, root, word):
        return \
            not word \
            or word[0] in root \
            and self._contains(root[word[0]], word[1:])

    def __contains__(self, word):
        return self._contains(self._root, word)

if __name__ == '__main__':
    words = ['hello', 'hey', 'what', 'when', 'why']
    trie = Trie(words)
    print('Is "hello" in "words"? {}'.format('hello' in trie))
    print('Is "hellow" in "words"? {}'.format('hellow' in trie))
