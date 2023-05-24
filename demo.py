# Nested Lists
data = [
    {"date":"06-04-19", "weather": [{"description":"sunny", "temp":85, "wind":2}], "rain": False},
    {"date":"06-05-19", "weather": [{"description":"cloudy", "temp":75, "wind":22}], "rain": False},
    {"date":"06-06-19", "weather": [{"description":"sunny", "temp":85, "wind":3}], "rain": False}
]

# # Accessing
# print(data[0]["date"])
# print(data[0]["weather"][0]["description"])

# # Two ways to traverse
# for entry in data:
#     print(data)

# for i in range(0, len(data)):
#     print(data[i])

# # Sorting with lambda
# data.sort(key = lambda entry : entry["weather"]["temp"])

# # Sets
# # Cannot have duplicate values
# my_set = {1, 0, 2, 5, "d"}
# # Type casting with set() can be used to remove dups
# # ORDER is not preserved
# vals = [4,4,1,1,1,125,2,3,4,4,2,1]
# print(set(vals))

# # List Comprehension
# # Lets you transform a list

# # ex: an operation
# new_vals = [num**2 for num in vals]
# print("New Values List Comp: " + new_vals)

# # ex: a function
# other_vals = [
#     [3,4,3,2,4,4],
#     [3,4,8,2,0,4],
#     [1,3,9,3,7,6]
# ]

# new_other = [sum(vals) for vals in other_vals]
# print("New other List Comp: " + new_other)