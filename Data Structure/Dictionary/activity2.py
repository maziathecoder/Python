test_dict = {   
    'codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1
}
print("the original dictionary : " + str(test_dict))
k = 2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("frequency of k is : " + str(res))