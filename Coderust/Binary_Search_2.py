""" 
Iterative Solution for Binary Search :
Runtime Complexity
Logarithmic, O(logn).

Memory Complexity
Constant, O(1).

"""

def binary_search_iterative(a, key):
  
  low = 0
  high = len(a) - 1
  
  while low <= high:
    mid = low + ((high - low) // 2)
    if a[mid] == key:
      return mid
    if key < a[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return -1

def linear_search(a, key):
  for i in range(0,len(a)):
    if a[i] == key:
      return i
  return -1

def test_bin_search(arr, key, expected):
  arr.sort()  
  i = linear_search(arr, key)
  j = binary_search_iterative(arr, key)

  assert i == j

  if expected == True:
    assert j >= 0
  else:
    assert j == -1
  
  print("Linear Search Key found at ",str(i)) 
  print("Binary Search Key found at ",str(j))

def main():
  arr = [5, 3, 2, 9, 7]
  test_bin_search(arr, 5, True)
  test_bin_search(arr, 15, False)
  test_bin_search([], 100, False)
  test_bin_search([55], 50, False)
  test_bin_search([55], 55, True)
  
  print("********Complete*******")

main()