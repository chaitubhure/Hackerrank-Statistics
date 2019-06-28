# Enter your code here. Read input from STDIN. Print output to STDOUT

size=int(input())
numbers=list(map(int,input().split()))
weights=list(map(int,input().split()))


sum_array = 0
for i in range(size):
    sum_array = sum_array + (numbers[i]*weights[i])


print(round(sum_array/sum(weights),1))
