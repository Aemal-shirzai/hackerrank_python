# to get palindromic: We can get by 10 to power of n, divided by 9 this will get us the number of ones and these once with power of 2 will
# get us the palindromic triangle.

for i in range(1, int(input()) + 1):
     print (pow(pow(10, i) // 9, 2))