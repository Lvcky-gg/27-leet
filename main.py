

def removeElement(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = '_'
    while '_' in nums:
        nums.remove('_')
    return nums



def remove_elements(nums, val):
    pointer = len(nums) - 1
    while pointer >= 0:
        if nums[pointer] == val:
            nums.pop(pointer)
            # nums[pointer:len(nums) - 1] = nums[pointer + 1:len(nums)]
        pointer -= 1
    return nums


print(removeElement([3, 2, 2, 3], 3))
print(remove_elements([3, 2, 2, 3], 3))