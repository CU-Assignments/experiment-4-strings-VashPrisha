def camelMatch(queries, pattern):
    result = []
    for query in queries:
        if isMatch(query, pattern):
            result.append(True)
        else:
            result.append(False)
    return result

def isMatch(query, pattern):
    i, j = 0, 0
    while i < len(query) and j < len(pattern):
        if query[i] == pattern[j]:
            i += 1
            j += 1
        elif query[i].isupper():
            return False
        else:
            i += 1
    return j == len(pattern) and all(c.islower() for c in query[i:])
