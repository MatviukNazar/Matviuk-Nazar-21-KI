lst = ["list", 23, 2.4, 56, 456] 
tp = [type(value) for value in lst] 
from collections import Counter 
mst_type = Counter(tp).most_common() 
print(Counter(tp)) 
print(mst_type[0])