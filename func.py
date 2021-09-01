def most_frequent(str):
    d = dict()
    for key in str:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d


S = input("Please enter a string ")
Dict = most_frequent(S)

for key in Dict:
    print(f"{key} = {Dict[key]}")


