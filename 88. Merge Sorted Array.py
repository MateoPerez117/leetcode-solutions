# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6] 
n = 3

i = m -1
j = n -1
k = m + n - 1

if n == 0:
    print (nums2)
elif m == 0:
    print (nums1)
else:
    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
print(nums1)