# Dieudonne Muhirwa M14185704
# Allen Detmer M15216736
# JiaBin Chang M13782945
# Joseph Matawaran M15228497

# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

import unittest
import time

# Bubble Sort
# The param is a list
def bubbleSort(list):
    # first find the size of the array
    size = len(list)

    # loop through all array elements
    for location1 in range(size):
        for location2 in range(0, size - location1 - 1):
            if list[location2] > list[location2 + 1]:
                temp = list[location2]
                list[location2] = list[location2 + 1]
                list[location2 + 1] = temp
    return list


# Quick Sort
# The parameter is a list

def quickSort(list):
    if len(list) <= 1:
        return list

    # selecting a pivot point in the list
    pivot = list[len(list) // 2]

    '''partition all elements into a right (element greater than pivot), 
    middle (element equal to the pivot), and left (element smaller than pivot)
    while looping so that all elements will recursively sort and combine'''
    right = [x for x in list if x > pivot]
    mid = [x for x in list if x == pivot]
    left = [x for x in list if x < pivot]

    return quickSort(left) + mid + quickSort(right)


def merge(left, right):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result + left if len(left) else result + right
    return result

def mergeSort(list):
    if len(list) < 2:
        return list

    mid = len(list) // 2
    leftlist = list[:mid]
    rightlist = list[mid:]

    return merge(mergeSort(leftlist), mergeSort(rightlist))

def hybridSort(L, BIG, SMALL, T):
    if len(L) > T:
        if BIG == "mergeSort":
            # hybridsort for large list baheve like mergesort
            mid = len(L) // 2
            leftList = L[:mid]
            rightList = L[mid:]
            return merge(hybridSort(leftList, BIG, SMALL, T),
                         hybridSort(rightList, BIG, SMALL, T))
        elif BIG == "quickSort":
            # hybridsort for large lists behave like quicksort
            first = 0
            last = len(L) - 1
            pivot = L[len(L) // 2]
            '''partition all elements into a right (element greater than pivot), 
            middle (element equal to the pivot), and left (element smaller than pivot)
            while looping so that all elements will recursively sort and combine'''
            right = [x for x in L if x > pivot]
            mid = [x for x in L if x == pivot]
            left = [x for x in L if x < pivot]
            return hybridSort(left, BIG, SMALL, T) + mid + hybridSort(right, BIG, SMALL, T)
        else:
            print
            "input value for BIG search is not valid returninng None"
            return None
    else:
        if SMALL == "bubbleSort":
            return bubbleSort(L)
        else:
            print
            "input value for SMALL search is not valid returninng None"
            return None

# compute the sorting time
def computeTime(L, BIG, SMALL, T):
    if BIG == "quickSort" and SMALL == "bubbleSort":
        t1 = time.process_time_ns()
        result = hybridSort(L, "quickSort", "bubbleSort", T)
        t2 = time.process_time_ns()
        print(f'Hybrid Sort({BIG}, {SMALL}) execution time: {t2-t1} ns')
    elif BIG == "mergeSort" and SMALL == "bubbleSort":
        t1 = time.process_time_ns()
        result = hybridSort(L, "mergeSort", "bubbleSort", T)
        t2 = time.process_time_ns()
        print(f'Hybrid Sort({BIG}, {SMALL}) execution time: {t2-t1} ns')
    else:
        print("input value for SMALL search is not valid returninng None")
        return None
    return result

class SortingTest(unittest.TestCase):
    def test_01(self):
        print("TestCase01\n")
        L = []
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([], result)

        L = []
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([], result)
        print("\n")

    def test_02(self):
        print("TestCase02\n")
        L = [-1, -14]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-14, -1], result)

        L = [-1, -14]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-14, -1], result)
        print("\n")

    def test_03(self):
        print("TestCase03")
        L = [-2, 0, 0]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-2, 0, 0], result)

        L = [-2, 0, 0]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-2, 0, 0], result)
        print("\n")

    def test_04(self):
        print("TestCase04")
        L = [-7, 0, 3, 0]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-7, 0, 0, 3], result)

        L = [-7, 0, 3, 0]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-7, 0, 0, 3], result)
        print("\n")

    def test_05(self):
        print("TestCase05")
        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)

        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)
        print("\n")

    def test_06(self):
        print("TestCase06")
        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)

        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)
        print("\n")

    def test_07(self):
        print("TestCase07")
        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)

        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)
        print("\n")

    def test_08(self):
        print("TestCase08")
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)

        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)
        print("\n")

    def test_09(self):
        print("TestCase09")
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0],
                         result)

        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0],
                         result)
        print("\n")
    
    def test_10(self):
        print("TestCase10")
        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394],
                        result)

        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394],
                        result)
        print("\n")

    def test_11(self):
        print("TestCase11")
        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687],
                         result)

        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687],
                         result)
        print("\n")

if __name__ == '__main__':
    unittest.main()

'''
Test case design
Based on ISP(Input Space Partitioning) and ECC(Each Choice Coverage)

1. List length is 0
L = []

2. List length is less than 5 and contains all negative numbers
L = [-1,-14]

3. List length is less than 5 and contains negative numbers and zeros
L = [-2,0,0]

4. List length is less that 5 and contains negative numbers, positive numbers, and zeros
L = [-7, 0, 3, 0]

5. List length is equal to 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33]

6. List length is equal to 5 and contains negative numbers and zeros
L = [-1000, -39, 0, -36, 0]

7. List length is equal to 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0, 200, -999]

8. List length is more then 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33, -30003, -30444, -273]

9. List length is more than 5 and contains negative numbers and zeros
L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]

10. List length is more that 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]

11. List length is 100 and are random numbers for -99999 to 99999
L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
-36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
-6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
-4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]

Testing Results

TestCase01

Hybrid Sort(quickSort, bubbleSort) execution time: 4000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 1000 ns


.TestCase02

Hybrid Sort(quickSort, bubbleSort) execution time: 2000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 1000 ns


.TestCase03
Hybrid Sort(quickSort, bubbleSort) execution time: 2000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 1000 ns


.TestCase04
Hybrid Sort(quickSort, bubbleSort) execution time: 3000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 2000 ns


.TestCase05
Hybrid Sort(quickSort, bubbleSort) execution time: 3000 ns
Hybrid Sort(quickSort, bubbleSort) execution time: 2000 ns


.TestCase06
Hybrid Sort(quickSort, bubbleSort) execution time: 2000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 3000 ns


.TestCase07
Hybrid Sort(quickSort, bubbleSort) execution time: 2000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 2000 ns


.TestCase08
Hybrid Sort(quickSort, bubbleSort) execution time: 6000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 6000 ns


.TestCase09
Hybrid Sort(quickSort, bubbleSort) execution time: 6000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 6000 ns


.TestCase10
Hybrid Sort(quickSort, bubbleSort) execution time: 13000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 11000 ns


.TestCase11
Hybrid Sort(quickSort, bubbleSort) execution time: 139000 ns
Hybrid Sort(mergeSort, bubbleSort) execution time: 122000 ns


.
----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK

'''