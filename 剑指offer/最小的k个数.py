def GetLeastNumbers_Solution(tinput, k):
    # write code here
    left = 0
    right = len(tinput) - 1

    def quicksort(tinput, left, right, k):
        key = tinput[left]
        while left < right:
            while left < right and tinput[right] > key:
                right = right - 1
            tinput[left] = tinput[right]
            while left < right and tinput[left] < key:
                left = left + 1
            tinput[right] = tinput[left]
        tinput[left] = key
        if left == k - 1:
           return sorted(tinput[0:left + 1])
        elif left < k - 1:
            return quicksort(tinput, left + 1, len(tinput) - 1, k )
        else:
            return quicksort(tinput, 0, left - 1, k )

    return quicksort(tinput, left, right, k)

print(GetLeastNumbers_Solution([4,2,1,6,2,7,3,8],6))