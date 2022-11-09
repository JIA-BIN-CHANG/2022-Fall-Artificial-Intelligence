import unittest
# data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23, -20, -3, 2]

def merge(left, right):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result

def mergeSort(list):
    if len(list) < 2:
        return list

    mid = len(list)//2
    leftlist = list[:mid]
    rightlist = list[mid:]

    return merge(mergeSort(leftlist),mergeSort(rightlist))

class SortingTest(unittest.TestCase):
    def test_01(self):
        L = []
        self.assertEqual([], mergeSort(L))

    def test_02(self):
        L = [-1,-14]
        self.assertEqual([-14,-1], mergeSort(L))

    def test_03(self):
        L = [-2,0,0]
        self.assertEqual([-2,0,0], mergeSort(L))

    def test_04(self):
        L = [-7, 0, 3, 0]
        self.assertEqual([-7,0,0,3], mergeSort(L))
    
    def test_05(self):
        L = [-99, -5, -34, -29, -33]
        self.assertEqual([-99,-34,-33,-29,-5], mergeSort(L))
    
    def test_06(self):
        L = [-1000, -39, 0, -36, 0]
        self.assertEqual([-1000,-39,-36,0,0], mergeSort(L))
    
    def test_07(self):
        L = [10000, -3, 0 , 200, -999]
        self.assertEqual([-999,-3,0,200,10000], mergeSort(L))

    def test_08(self):
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        self.assertEqual([-30444,-30003,-273,-99,-34,-33,-29,-5], mergeSort(L))
    
    def test_09(self):
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        self.assertEqual([-999384,-392930,-387474,-93984,-3984,-1000,-39,-36,0,0], mergeSort(L))

    def test_10(self):
        L = [10000, -3, 0 , 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        self.assertEqual([-394874,-999,-3,0,0,0,2,34,200,3004,3948,10000,83874,928394], mergeSort(L))

if __name__ == '__main__':
    unittest.main()

'''
Test cases design
Based on ISP(Input Space Partitioning) and ECC(Each Choice Coverage)

1. length is 0
L = []

2. length is less than 5 and contains all negative numbers
L = [-1,-14]

3. length is less than 5 and contains negative numbers and zeros
L = [-2,0,0]

4. length is less that 5 and contains negative numbers, positive numbers, and zeros
L = [-7, 0, 3, 0]

5. length is equal to 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33]

6. length is equal to 5 and contains negative numbers and zeros
L = [-1000, -39, 0, -36, 0]

7. length is equal to 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0, 200, -999]

8. length is more then 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33, -30003, -30444, -273]

9. length is more than 5 and contains negative numbers and zeros
L = [-1000, -39, 0 -36, 0, -3984, -93984, -392930, -387474, -999384]

10. length is more that 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0 , 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]

'''