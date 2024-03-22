def solution(myString, pat):
    lowMystr = myString.lower()
    lowPat = pat.lower()
    
    if lowPat in lowMystr:
        return 1
    else:
        return 0