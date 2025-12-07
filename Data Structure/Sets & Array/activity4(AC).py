set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
sym_diff = set1.symmetric_difference(set2)
sym_diff_op = set1 ^ set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference (method):", sym_diff)
print("Symmetric Difference (^ operator):", sym_diff_op)