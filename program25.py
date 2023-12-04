#wapp to the recursion of digit sum
#test case 1                  test case 2
# n = 148                         n=9875
# k = 3                             k= 4
# output                       output
#3                                8
# logic
#
# 1+4+8+1+4+8+1+4+8         9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5
# 39                           116
# 3+9                           1+1+6
#12                                 8 output
# 1+2=3 output



def recursive_digit_sum(n,k):
    def digit_sum(num):
        if num< 10:
            return num
        else:
            return num%10 + digit_sum(num//10)
    initial_sum = digit_sum(n)*k
    if initial_sum>9 and k >=1:
        return recursive_digit_sum(initial_sum,1)
    else:
        return initial_sum
n=148
k=3
result=recursive_digit_sum(n,k)
print(result)  