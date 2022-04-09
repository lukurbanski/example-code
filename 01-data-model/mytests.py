def lenbyo(x):
    if x.count("o") == 0:
        ln = 0
    else: 
        ln = len(x)/x.count("o")
    return ln


print(list(map(lenbyo, ["cos","wodnik","kolorowanka", "kiermasz"])))

print(list(map(sum,zip([1,2,3],[5,3,2]))))