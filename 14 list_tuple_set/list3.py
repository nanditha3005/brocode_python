# using above list find a number wch prints first thirce numbers

lst=[100,20,30,5,6,20,100,20,5,100,6,30]
from collections import Counter

count=Counter(lst)
for num in lst:
    if count[num]==3:
        print(f"The first number that apperars exactly three times is :{num}")
        break



# 100 appears at positions → index 0, 6, 9 → 3 times
# 20 also appears 3 times (positions 1, 5, 7)
# But 100 appears first in the list, so it is returned first when we iterate in order.