Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(my_list):
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list[i]="big"
    return my_list
print(biggie_size([-1,3,5,-5]))
Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_postive(nums_list):
    count=0
    for val in range(len(nums_list)):
        if nums_list[val] > 0:
            count +=1
    last_val=len(nums_list)-1
    nums_list[last_val]=count
    return nums_ list
print(count_postive([1,6,-4,-2,-7,-2]))
Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7
def sum_total(my_list):
    total = 0
   for idx in range(0,len(my_list)):
       total= total + my_list[idx]
   return total
    
print(sum_total([1,2,3,4]))
Average - Create a function that takes a list and returns the average of all the values.
Example: average([1,2,3,4]) should return 2.5
def average(my_list):
  total = 0
  avg=0
  for idx in range(0,len(my_list),1):
      total= total + my_list[idx]
  avg= total / len(my_list)
  return avg
    
print(average([1,2,3,4]))

Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0

def length(nums_list):
    for i in range(0, len(nums_list)):
        return len(nums_list)
print(length([2,3,4]))
Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
def minimum(nums_list):
    num_list_min=nums_list[0]
    for idx in range(0,len(nums_list),1):
       if nums_list[idx] < num_list_min:
           num_list_min=nums_list[idx]
    return num_list_min
print(minimum([37,2,1,-9]))
Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.#Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False
def maximum(nums_list):
    num_list_max=nums_list[0]
    for idx in range(0,len(nums_list),1):
      if nums_list[idx]>num_list_max:
            num_list_max=nums_list[idx]
        return num_list_max
print(maximum([37,2,1,-9]))
Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(nums_list:
    total = sum_total(nums_list)
    avg = average(nums_list)
    min = minimum(nums_list)
    max = maximum(nums_list)
    leng = length(nums_list)

    ultimate= {'sumTotal':total, 'average':avg, 'minimum': min, 'maximum': max, 'length': leng
    }
    return analysis

print(ultimate_analysis([37,2,1,-9]))
Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(nums_list):
    return nums_list[::-1]
print(reverse_list([37,2,1,-9]))















