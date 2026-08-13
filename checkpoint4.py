from functools import reduce
numbers = [2, 3, 6]
result = reduce(lambda x, y: x * y, numbers)
print(f"Result = {result}") 

def sort_by_last_element(tuple_list):
    # The key tells Python what to sort by.
    # lambda t: t[-1] returns the last item of each tuple.
    return sorted(tuple_list, key=lambda t: t[-1])
sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_by_last_element(sample)
print("Expected result :", result)


def combine_dicts(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
        return result
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined = combine_dicts(d1, d2)
print("Expected result:", combined)


def generate_squares(n):
    squares = {}
    for i in range(1, n + 1):
    
        squares[i] = i * i
    return squares
n = int(input("Enter a number: "))
result = generate_squares(n)
print(result)

items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(items, key=lambda t: float(t[1]), reverse=True))

my_set = {1, 2, 3}
print("Original set:", my_set)
my_set.add(4)
print("After adding 4:", my_set)
my_set.update([5, 6])
print("After adding 5 and 6:", my_set)
my_set.remove(2)
print("After removing 2:", my_set)
my_set.discard(10)  

my_set.discard(3)
print("After discarding 3:", my_set)
popped = my_set.pop()
print(f"Removed {popped}, set is now:", my_set)
my_set.clear()

print("After clearing:", my_set)
