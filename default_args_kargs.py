# def sum(num1,num2,num3=0):
#     result = num1 + num2 + num3
#     return result

# total = sum(99,11,5)
# print('total:',total)
# args
# def all_sum(num1,num2,*numbers):
#     print(numbers)
#     sum = 0
#     for num in numbers:
#         print(num)
#         sum = sum + num
#     return sum   
# total = all_sum(45,46,89,11,81,5,2,77)

# print('all sum:',total)

def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum
total = all_sum(1,2,3,4,5,6,7,8,9)

print('Total numbers is:',total)