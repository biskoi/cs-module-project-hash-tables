class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0

        for item in self.storage:
            if item is None:
                continue

            curr_node = item
            while item is not None:
                count += 1
                item = item.next
        
        return count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        seed = 0
        fnv_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash_ = offset_basis + seed
        for x in key:
            hash_ = hash_ * fnv_prime
            hash_ = hash_ ^ ord(x)

        return hash_


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        # self.storage[hash_index] = value
        if self.storage[hash_index] is None:
            self.storage[hash_index] = HashTableEntry(key, value)
        else:
            item = self.storage[hash_index]
            prev = self.storage[hash_index]
            while item is not None:
                if item.key is key:
                    item.value = value
                    return
                else:
                    prev = item
                    item = item.next
            
            if item is None and prev.key is not key:
                prev.next = HashTableEntry(key, value)    


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.storage[hash_index] is None:
            print('Key not found.')
        else:
            item = self.storage[hash_index]
            prev = None
            while item is not None:
                if item.key == key:
                    print('found key', item.key)
                    item.value = None
                    if item.next is None and prev is None:
                        self.storage[hash_index] = None
                        return
                    elif prev is not None:
                        prev.next = None

                prev = item
                item = item.next
            
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.storage[hash_index] is None:
            return None
        else:
            item = self.storage[hash_index]
            while item is not None:
                if item.key == key:
                    return item.value
                
                item = item.next
            
            return None
                    
            


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        new_ht = HashTable(new_capacity)

        for item in self.storage:
            if item is None:
                continue

            curr_node = item
            while curr_node is not None:
                new_ht.put(curr_node.key, curr_node.value)
                curr_node = curr_node.next

        self.capacity = new_capacity
        self.storage = new_ht.storage





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("asd")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
