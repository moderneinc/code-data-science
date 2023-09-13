class UniqueDictionaries:
    """
    Class used similar to a set but for dictionaries. The class is used to
    ensure that dictionaries are unique based on their key/value pairs.
    """

    def __init__(self):
        self._data = []  # list to store actual dictionaries
        self._hashes = set()  # set to store hashes for uniqueness check

    def add(self, d):
        h = hash(frozenset(d.items()))
        if h not in self._hashes:
            self._hashes.add(h)
            self._data.append(d)

    def to_list(self):
        return self._data

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __contains__(self, d):
        h = hash(frozenset(d.items()))
        return h in self._hashes
