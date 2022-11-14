import pickle
l = ['a', 'b', 'c']

#pickling
with open("abc.txt", 'wb') as f:
    pickle.dump(l, f)

# unpickling
pickleOff = open('abc.txt', 'rb')
gt = pickle.load(pickleOff)
print(gt)
