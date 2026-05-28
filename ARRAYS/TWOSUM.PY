#FIRST TRY TO RECOGNIZE THE PATTERN 
#UNDERSTAND THE PROBLEM STATEMENT
#THINK OF A SOLUTION
#TRY A DRY RUN
#JUST CODE IT
#TIME COMPLEXITY O(N^2) AND SPACE COMPLEXITY O(1)
#FUNCTIONS***

"""Precise Summary:

✅ TwoSum 3 tarike se solve hoti hai
✅ Hashmap = Best optimized — kisi bhi array pe kaam karta hai
✅ Two Pointer = Sirf sorted array pe kaam karta hai
✅ Brute Force = Sabse slow — har combination check karta hai

Array sorted hai?
├── Haan → Two Pointer (space bhi bachta hai)
└── Nahi → Hashmap (safest & optimized)"""

#BRUTE FORCE UNSORTED PE 
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]  
            
nums=[10,7,6,15] #input argument
target=16        #input argument
print(twosum(nums,target))    #function call

# method 2: USING HASHMAP
#TIME COMPLEXITY O(N) AND SPACE COMPLEXITY O(N)
def twosum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[nums[i]]=i

nums=[10,7,6,15] #input argument
target=16        #input argument
print(twosum(nums,target))    #function call     



## method 3: USING TWO POINTERS
#TIME COMPLEXITY O(NlogN) AND SPACE COMPLEXITY O(1)
def twosum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
    


