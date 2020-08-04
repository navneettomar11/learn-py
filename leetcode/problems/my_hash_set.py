class MyHashSet:

    def __init__(self):
        self.key_space = 2096
        self.hash_table=[[] for i in range(self.key_space)]

    def add(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key] = key

    def remove(self, key):
        hash_key=key%self.key_space
        del self.hash_table[hash_key]

    def contains(self, key):
        hash_key=key%self.key_space
        return self.hash_table[hash_key] == key


if __name__ == "__main__":

    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    hashSet.add(3)
    print(hashSet.contains(2))
    hashSet.remove(2)
    print(hashSet.contains(2))
