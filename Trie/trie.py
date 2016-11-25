class Trie:
    def __init__(self, words, end_of_word=''):
        self._root = {}
        self._EOW = end_of_word
        for word in words:
            self._add_word(self._root, word)

    def _add_word(self, root, word):
        if word:
            descendent = root.setdefault(word[0], {})
            self._add_word(descendent, word[1:])
        else:
            root[self._EOW] = self._EOW

    def _contains(self, root, word):
        return \
            not word and self._EOW in root \
            or word and word[0] in root \
            and self._contains(root[word[0]], word[1:])

    def __contains__(self, word):
        return self._contains(self._root, word)

if __name__ == '__main__':
    words = ['hello', 'hey', 'what', 'when', 'why']
    trie = Trie(words)
    assert 'hello' in trie, '"hello" should be in the Trie'
    assert 'hellow' not in trie, '"hellow" shouldn\'t be in the Trie'
    assert 'hel' not in trie, '"hel" shouldn\'t be in the Trie'
    assert '' not in trie, '"" shouldn\'t be in the Trie'
