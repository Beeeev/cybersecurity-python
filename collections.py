from collections import ChainMap
dict1 = {"first value": 1, "second value": 2}
dict2 = {"third value": 3, "fourth value": 4}
cm = ChainMap(dict2, dict1)

for key, value in cm.items():
    print(key, value)
    
