n = int(input())
numbers = [int(x) for x in input().split(' ', n-1)]
i = 0
sum1 = 0
for i in range(n):
    sum1 = sum1 + numbers[i]
avg = sum1/n
print('%.3f' % avg)
