l = [5,6,3,7,9,2,8,1,4,0,11]
print("original list: ",l)
count = 0
for i in l:
    count = count + i
average = count/len(l)
print("sum= ",count)
print("average= ",average)
l.sort()
print("smallest element is: ",l[0])
print("largest element is: ",l[-1])