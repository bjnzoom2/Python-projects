dictionary = {
    "a" : 1234,
    "banana" : "akjd",
    "zepto" : 0.000000000000000000001
}

print(dictionary["zepto"])
dictionary.update({"Germany" : "Berlin"})
dictionary.pop("a")

print(dictionary)

print("\n")
for i, j in dictionary.items():
    print(i, j)