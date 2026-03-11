nums1 = [1,2,3]
nums2 = [2,4,6]
ans1 = []
ans2 = []

for i in range(len(nums1)):
    if nums1[i] not in nums2 and nums1[i] not in ans1:
        ans1.append(nums1[i])

for i in range(len(nums2)):
    if nums2[i] not in nums1 and nums2[i] not in ans2:
        ans2.append(nums2[i])      
    
print (ans1, ans2)

