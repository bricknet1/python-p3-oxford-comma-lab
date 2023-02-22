def oxford_comma(items):
    if len(items) == 1:
        print(''.join(items))
        return ''.join(items)
    elif len(items) == 2:
        print(' and '.join(items))
        return ' and '.join(items)
    else:
        names = ', '.join(items[0:-1])
        names += f", and {items[-1]}"
        print(names)
        return names


oxford_comma(["the rest"])
oxford_comma(["Little Marge", "the rest"])
oxford_comma(["Little Bart", "Little Lisa", "Little Marge", "the rest"])