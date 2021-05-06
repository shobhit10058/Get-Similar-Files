from fuzzywuzzy import fuzz
import os, sys

def Search(Iterator, query):
    query = query.lower()
    strings = [s for s in Iterator]

    tar = [strings[0] for _ in range(5)]
    ini = [0 for _ in range(5)]

    for s in strings:
        if(s[0] == '.'):
            continue
        ps = fuzz.partial_ratio(s.lower(), query)
        for i in range(len(ini)):
            if(ps > ini[i]):
                ini[i + 1: ] = ini[i: -1]
                tar[i + 1: ] = tar[i: -1]
                tar[i] = s
                ini[i] = ps
                break

    print("\nThe most similar are:")
    for i in range(len(ini)):
        if(ini[i] > 0):
            print(tar[i])

if(len(sys.argv) > 0):
    Search(os.listdir(os.getcwd()), " ".join(sys.argv[1:]))
