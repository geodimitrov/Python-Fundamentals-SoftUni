def even_odd(*args):
    nums = []
    for el in args:
        if isinstance(el, str):
            command = el
        else:
            nums.append(el)

    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, nums))
    else:
        result = list(filter(lambda x: x % 2 != 0, nums))
    return result