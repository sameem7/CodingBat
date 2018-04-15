#Given an array of ints, return the sum of the first 2 elements in the array. 
#If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
  
  #function to add the 2 elements in the list
  def sumList(nums, length):
    result = 0
    for i in range (length):
      result = result + nums[i]
    
    return result
  
  #call the adding function with appropriate arguments depending on the length of the original list
  if (len(nums) < 2):
    return (sumList (nums, len(nums)))
  else:
    return (sumList(nums[0:2], 2)) #Slice the first 2 elements if list is of length >2
