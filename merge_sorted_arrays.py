def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays nums1 and nums2 into nums1 in-place.

    Args:
        nums1: First sorted array with length m+n (last n elements are 0s)
        m: Number of actual elements in nums1
        nums2: Second sorted array with length n
        n: Number of elements in nums2

    The function modifies nums1 in-place and doesn't return anything.

    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    # Start from the end of both arrays
    # p1 points to the last element in nums1's initial elements
    # p2 points to the last element in nums2
    # p points to the last position in nums1
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Merge from the end to avoid overwriting elements
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    # (no need to copy remaining nums1 elements as they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Test 1: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]

    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"Test 2: {nums1}")  # Expected: [1]

    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Test 3: {nums1}")  # Expected: [1]

    # Test case 4
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Test 4: {nums1}")  # Expected: [1, 2, 3, 4, 5, 6]

    # Test case 5
    nums1 = [1, 2, 4, 5, 6, 0]
    m = 5
    nums2 = [3]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Test 5: {nums1}")  # Expected: [1, 2, 3, 4, 5, 6]
