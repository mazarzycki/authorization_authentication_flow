def add_up(obj, ints=0, letters=""):
    for elem in obj:
        if isinstance(elem, int):
            ints += elem
        elif isinstance(elem, str):
            letters += elem
        elif isinstance(elem, dict):
            keys, values = zip(*elem.items())
            ints, letters = add_up(keys, ints, letters)
            ints, letters = add_up(values, ints, letters)
        elif isinstance(elem, list):
            ints, letters = add_up(elem, ints, letters)    
    return ints, letters

# Test cases
obj1 = ["A", "B", "CD", "EF", "G", "H", "I"]
print(add_up(obj1))

obj2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(add_up(obj2))

obj3 = ["A", 1, "B", 2, 3, "CD", "EF", 4, "G", 5, "H", 6, 7, "I", 8]
print(add_up(obj3))

obj4 = ["A", 1, "B", [2, 3], ["CD", "EF"], 4, "G", [5, 6, ["H", "I"], 7, [8]]]
print(add_up(obj4))

obj5 = ["A", 1, "B", {2: 3}, ["CD", "EF"], 4, [{"G": {"H": "I"}}], [5, {6: 7}, [8]]]
print(add_up(obj5))

obj6 = ["A", 1, "B", [2, 3], ["CD"], 4, {"E": "F", "G": [[[{"H": ["I"]}]]]}, [5, 6, 7, [8]]]
print(add_up(obj6))
