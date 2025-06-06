# Iterating Lists
The most elegant way to iterate over a list by index in Python is to use the built-in range() function with len():
```
for i in range(len(my_list)):
    # Access element with my_list[i]
    print(i, my_list[i])
```
If you need both the index and the value, enumerate() is more Pythonic:
```
for i, value in enumerate(my_list):
    print(i, value)
```