# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    s = input()
    even = s[0::2]
    odd = s[1::2]
    print(even,odd)
