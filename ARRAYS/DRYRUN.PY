#BRUTE FORCE APPROACH (WOKS ON UNSORTED ARRAY)
#jab j ka loop khatam hota hai, control automatically outer i loop pe wapas aa jata hai.
def twosum(nums, target):
    for i in range(len(nums)):  #yaani i start se last index tak chalega
        for j in range(i+1,len(nums)): #Har ek i ke liye j apna poora loop complete karega
            if nums[i]+nums[j]==target:
                return[i,j]
            
nums=[10,7,6,15] #input argument
target=16        #input argument
print(twosum(nums,target))    #function call 


# method 2: USING HASHMAP
#jab complement hashmap me milta hai, toh uska index aur current index return karte hain.
def twosum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[nums[i]]=i
nums=[10,7,6,15] #input argument
target=25       #input argument
print(twosum(nums,target))    #function call        

## method 3: USING TWO POINTERS (works only on sorted array)
#jab current sum target ke barabar hota hai, toh left aur right pointer ke index
#jab current sum target se chhota hota hai, toh left pointer ko aage badhate hain
#jab current sum target se bada hota hai, toh right pointer ko peeche le jate hain
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
nums=[10,7,6,15] #input argument
target=16        #input argument
print(twosum(nums,target))    #function call            


#hashmap>>two pointer>brute force
#time complexity: hashmap O(N), two pointer O(NlogN), brute force O(N^2)