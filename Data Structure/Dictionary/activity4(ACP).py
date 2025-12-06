test_dict = {'codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}
print("Test Dictionary:", test_dict)
value = int(input("Enter the value you want to check the frequency of: "))
frequency = list(test_dict.values()).count(value)
print("Frequency of value", value, "is:", frequency)