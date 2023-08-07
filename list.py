# list ,array,collection is same (simple terms)
#intdex =   0  1  2  3  4  5  6  7  8  9 
numbers = [45,56,12,89,87,32,89,59,46,93]
#intdex = -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
print(numbers[3],numbers[-3])

# list(start:end) -> start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])

#list(start : end :step)
print(numbers[1:7:1])
print(numbers[1:7:2])
# print(numbers[1:7:-1])   #hole kicoi ans pabo na
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[4:]) # sesh ta na dile start theke last pojjonto jabe
print(numbers[:5]) # prothom ta na dile ses pojontto jabe
print(numbers[:])  # kicoi na dile soru theke sesh pojjonto  ->short cut to copy a list
print(numbers[::-1]) # full list reverse hoea jabe   -> short cut to reverse list
