# Insertion Sort
# efficient for sorting a small number of elements
# running time: O(n^2)

def insertionSort(items):
    # Loop through the list the number of times equal to the length of the list
    # Any item in the list to the left of the unsortedIndex will be sorted,
    # any item to the right will be unsorted
    for unsortedIndex in range(len(items)):
        # Store the item at unsortedIndex as the key, or item to be sorted
        key = items[unsortedIndex]
        # Begin the sortedIndex at one index less than the unsortedIndex
        sortedIndex = unsortedIndex - 1
        # Compare each item moving down the list until the sortedIndex equals zero
        # and while the item is greater than the key item
        while sortedIndex > -1 and items[sortedIndex] > key:
            items[sortedIndex+1] = items[sortedIndex]
            sortedIndex -= 1
        # Place the key item into the list at its sorted location
        items[sortedIndex+1] = key
    # list is sorted
    return items
