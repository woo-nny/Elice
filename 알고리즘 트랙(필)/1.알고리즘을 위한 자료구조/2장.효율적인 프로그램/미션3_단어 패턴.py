def wordPattern(pattern, strList):
    patternSet = set(pattern)
    strListSet = set(strList)
    patternSetList = list(patternSet)
    strListSetList = list(strListSet)

    if len(pattern) != len(strList):
        return False

    if len(patternSetList) != len(strListSetList):
        return False

    patterSetListHash = {}

    for i in range(len(patternSetList)):
        patterSetListHash[patternSetList[i]] = strListSetList[i]

    strListArray = []
    for i in range(len(strList)):
        for ch in patterSetListHash:
            if strList[i] == patterSetListHash[ch]:
                strListArray.append(ch)

    strListArrayStr = ""
    for i in strListArray:
        strListArrayStr += i

    strListHash = {}
    patternHash = {}

    rerangeIndex = 0
    for ch in strList:
        if ch not in strListHash:
            strListHash[ch] = rerangeIndex
            rerangeIndex += 1

    rerangeIndex = 0
    for ch in pattern:
        if ch not in patternHash:
            patternHash[ch] = rerangeIndex
            rerangeIndex += 1

    strListCompare = []
    patternCompare = []

    for i in strList:
        for ch in strListHash:
            if i == ch:
                strListCompare.append(strListHash.get(ch))

    for i in pattern:
        for ch in patternHash:
            if i == ch:
                patternCompare.append(patternHash.get(ch))

    if strListCompare == patternCompare:
        return True
    else:
        return False




def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

if __name__ == "__main__":
    main()
