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

#replace("kmabckkkabckkkkabca", "abc", "gg")

def split(source, sep):
    list = []
    j = 0
    for i in range(len(source)):
        if sep == source[i]:
            list.append(source[j:i])
            j = i + 1
    list.append(source[j:])
    #print(list)

split("bb,cc,dd,ee", ",")


def split(source, sep):
    len_sep = len(sep)
    res = []
    idx = 0
    for i in range(0, len(source)):
        if source[i:i + len_sep] == sep:
            res.append(source[idx:i])
            idx = i + len_sep
    if len(source) > idx:
        res.append(source[idx:])
    return res

#print(split("aa,,bb,,cc,,dd", ",,"))



