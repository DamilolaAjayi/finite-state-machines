import random, collections

class NeetCodeGoogleInterview:

    def __init__(self):
        self.value_indexes = collections.defaultdict(list)
        self.values = []

    def insert_value(self, value):
        self.values.append(value)
        self.value_indexes[value].append(len(self.values) - 1)

    def remove(self, value):
        if value not in self.value_indexes:
            return

        last_val = self.values[-1] # last element in array
        index = self.value_indexes[value][-1] # index of element to remove
        self.values[index] = last_val
        
        self.value_indexes[last_val].append(index)
        self.values[-1] = value

        self.values.pop()

        self.value_indexes[value].pop()

    def get_random(self):
        return random.choice(self.values)
    
    def lookup(self,value):
        if value in self.values:
            return self.values[self.value_indexes[value][0]]
        else:
            # raise ValueError('Does not exist')
            return 'Does not exist'
    
test_values = NeetCodeGoogleInterview()

test_values.insert_value(1)
test_values.insert_value(2)
test_values.insert_value(3)
test_values.remove(1)
test_values.remove(2)
test_values.remove(3)
print(test_values.lookup(1))
print(test_values.lookup(2))
print(test_values.lookup(3))
# print(test_values.get_random())