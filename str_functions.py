def replace(source, old, new, count = None):
    length_source = len(source)
    length_old = len(old)
    result = ""
    if count == None:
        count = len(source)
    replace_count = 0
    i = 0
    while i < length_source:
        k = 0
        if source[i] == old[k] and i + length_old <= length_source and replace_count < count:
            j = i
            while j < i + length_old:
                if source[j] != old[k]:
                    break
                else:
                    k = k + 1
                j += 1
            if j == i + length_old:
                result += new
                i = j - 1
                replace_count += 1
            else:
                result += source[i]
        else:
            result += source[i]
        i += 1
    print(result)

replace("kmabckkkabckkkkabc", "abc", "gg", 2)