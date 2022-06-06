# Given a list, write a function that changes all positive numbers in the list to "big"
def biggie_size(b):
 for x in range(0,len(b),1):
     if b[x]>0:
         b[x]="big"
 return b        
print(biggie_size([-1, 3, 5, -5]))

 #Given a list of numbers, create a function to replace the last value with the number of positive values
def count_positives(b):
    count = 0
    for x in range(0,len(b),1):
        if b[x] > 0:
            count += 1
    b[len(b)-1] = count
    return b
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#Create a function that takes a list and returns the sum of all the values in the list

def sum_total(b):
    count = 0
    for x in range(0,len(b),1):
        count += b[x]
    return count
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#Create a function that takes a list and returns the average of all the values.x

def average(b):
    count = 0
    for x in range(0,len(b),1):
        count += b[x]
    return (count/len(b))
print(average([1,2,3,4]))

#Create a function that takes a list and returns the length of the list.
def length(b):
    b_length = 0
    for x in b:
        b_length += 1
    return b_length
print(length([37,2,1,-9]))
print(length([]))

#Create a function that takes a list of numbers and returns the minimum value in the list
def minimum(b):
    min = False
    if len(b) > 0:
        min = b[0]
        for x in range(0, len(b)):
            if b[x] < min:
                min = b[x]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

#Create a function that takes a list and returns the maximum value in the list.
def maximum(b):
    max = False
    if len(b) > 0:
        max = b[0]
        for x in range(0, len(b)):
            if b[x] > max:
                max = b[x]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

# Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list
def ultimate_analysis(b):
    b_analysis = {}
    b_analysis['sumTotal'] = sum_total(b)
    b_analysis['average'] = average(b)
    b_analysis['minimum'] = minimum(b)
    b_analysis['maximum'] = maximum(b)
    b_analysis['length'] = length(b)
    return b_analysis
print(ultimate_analysis([37,2,1,-9]))

 #Create a function that takes a list and return that list with values reversed
def reverse_list(b):
    temp = 0
    for x in range (0, int(len(b)/2)):
        temp = b[x]
        b[x] = b[len(b)-1-x]
        b[len(b)-1-x] = temp
    return b
print(reverse_list([37,2,1,-9]))
