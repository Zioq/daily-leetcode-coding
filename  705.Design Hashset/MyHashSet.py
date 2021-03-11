""" 
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
"""

class MyHashSet:
    
    def __init__(self):
        self.numBucket = 10000
        self.buckets = [[] for i in range(self.numBucket)]

    def create_hash(self,key):
        return key % self.numBucket
        
    def add(self, key):
        i = self.create_hash(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)
        
    def remove(self, key):
        i = self.create_hash(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key):
        i = self.create_hash(key)
        if key in self.buckets[i]:
            return True
        else:
            return False