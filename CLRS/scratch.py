count = 0

with open('scratch.txt', 'r') as f:
    for line in f.readlines():
        lst = line.split()
        count += len(lst)
    
print count
