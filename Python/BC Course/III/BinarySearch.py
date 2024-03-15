# looking for 1234567890
# omega = best case
# theta = average
# O = worst case -> log2(n)

n = 10**1000
target = -1
first = 0
last = n
count = 0

while first <= last :
    count += 1
    mid = (first + last)//2
    if mid == target :
        break
    elif mid > target :
        last = mid - 1
    else :
        first = mid + 1
print (count)