# Quicksort
# worst case running time: O(n^2)

# Uses Divide and Conquer to rearrange the items[lowIndex...highIndex] into two subarrays
#  items[lowIndex...midIndex-1] and items[midIndex+1...highIndex]
def quickSort(items, lowIndex, highIndex):
    if(lowIndex < highIndex):
        midIndex = partition(items, lowIndex, highIndex)
        quickSort(items, lowIndex, midIndex - 1)
        quickSort(items, midIndex + 1, highIndex)

# Rearranges the subarrays in place
#   return the computed midIndex
def partition(items, lowIndex, highIndex):
    i = lowIndex - 1
    for j in range(lowIndex, highIndex):
        if items[j] <= items[highIndex]:
            i += 1
            # exchange items[i] with items[j]
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
    # exchange items[i+1] with items[highIndex]
    temp = items[i+1]
    items[i+1] = items[highIndex]
    items[highIndex] = temp
    return i+1
