""" 
Recursive Solution for Binary Search :
Runtime Complexity
Logarithmic, O(logn).

Memory Complexity
Logarithmic, O(logn).
Recursive solution has O(logn) memory complexity as it will consume memory on the stack.

"""

def binary_search_rec(a, key, low, high):
  if low > high:
    return -1

  mid = low + ((high - low) // 2)
  
  if a[mid] == key:
    return mid
  elif key < a[mid]:
    return binary_search_rec(a, key, low, mid - 1)
  else:
    return binary_search_rec(a, key, mid + 1, high)

def binary_search(a, key):
  return binary_search_rec(a, key, 0, len(a) - 1)


def linear_search(a, key):
  for i in range(0,len(a)):
    if a[i] == key:
      return i
  return -1

def test_bin_search(arr, key, expected):
  arr.sort()  
  i = linear_search(arr, key)
  j = binary_search(arr, key)

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