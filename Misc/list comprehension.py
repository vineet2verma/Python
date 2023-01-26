
# List Comprehension

# Eg 1 Simple Way
l1 = [ i+1 for i in range(20) ]
print(l1)

# Eg 2 if condition
l2 = [ i for i in range(20) if i%2==0]
print(l2)
# Eg 3 Multiple if condition
l3 = [ i for i in range(20) if i%2==0 if i>0 if i<15]
print(l3)

# Eg 4 Multiple if condition
l4 = [ i for i in range(20) if i%2==0 if i>0 ]
print(l2)
