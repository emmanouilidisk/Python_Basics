def dedupe_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y
 
