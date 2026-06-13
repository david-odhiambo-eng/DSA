#creating a hash table form scratch
class HashTable:
    def __init__(self, size):
        #we use a list of list, inside each list we have a tuple
        #inside each tuple is a key-value pair
        #size is the number of lists within the list
        self.size = size
        self.bucket_list = []

    

    #creating a list of lists
    def create_buckets(self):
        for _ in range(self.size):
            self.bucket_list.append([])
        return self.bucket_list


    def hash_key(self, key)->int:
        #we carry out hashing(of the keys) by using a hash() function provided by python
        hashed_key = hash(key)
        #hashed_key can be any value from 1 to 1000000000
        #so we mod the result of the hash so that our indices are not out of range
        #the result of mod becomes the index of a bucket within our list of buckets
        bucket_index = hashed_key % self.size
        return bucket_index
    
    #adding a value(key-value)
    def add(self, key, value):
        #having the bucket_index, we can now locate the bucket itself in the list of buckets
        bucket = self.bucket_list[self.hash_key(key)]
        #a bucket is a tuple of (key1, value, key2, value2...and so on)
        for i in range(len(bucket)):
            #we are only interested in comparing the keys, at index [i][0]
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
        return bucket

    #getting a value using a key
    def get_value(self, key):
        bucket = self.bucket_list[self.hash_key(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                value = bucket[i][1]
                return value
        return 'No value'
            
    #updating a value using key
    def update(self, key, value):
        bucket = self.bucket_list[self.hash_key(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return bucket
        return 'Not updated'

    #deleting key - value
    def delete(self, key):
        bucket = self.bucket_list[self.hash_key(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return bucket
        return 'Not found'
    


table1 = HashTable(5)
print(f'Creating Buckets: {table1.create_buckets()}')
print(f'Adding: {table1.add(key='ENE221-0135/2022', value='DAVID ODHIAMBO')}'),
print(f'Getting: {table1.get_value(key='ENE221-0135/2022')}'),
print(f'Updated: {table1.update(key='ENE221-0135/2022', value='UPDATEDINDEX')}'),
print(f'Deleting: {table1.delete(key='ENE221-0135/2022')}')


        
