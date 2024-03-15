# |1|0.1|0.01|0.001|
for i in range (1, 4):
    print(f'|{1/(10**(i-1))}', end = "")
print(f'|{1/(10**(i))}|')

for i in range (1, 4):
    i = 1/(10**(i-1))
    print(f'|{i}', end = "")
print(f'|{i}|')
