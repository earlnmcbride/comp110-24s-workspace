"""Pratice with Dictionaires and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

# print out the keys that have true values
for key in in_stock:
    # key is going to be "carrots", "beets", "apples"
    # in_stock[key] is going to be True, False, True
    value: bool = in_stock[key]
    if in_stock[key] is True: # we don't actually need the "is true"
        print(key)