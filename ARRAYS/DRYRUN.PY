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

# question 1  #(Brute force approach)
def twosum(integers , target):
    for i in range(len(integers)):
     for j in range(i+1,len(integers)):
        if integers[i]+integers[j]==target:
            return[i,j]
        

integers=[1,2,3,4,5] #input argument
target=9            #input argument
print(twosum(integers,target))    #function call 

#method 2: two pointer approach(works only on sorted array)
def twosum(nums, target):
    left=0     #left pointor start se
    right=len(nums)-1     #right pointer end se
    while left<right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return[left,right]
        elif current_sum<target:
            left+=1
        else:
            right-=1
integers=[1,2,3,4,5] #input argument
target=9            #input argument
print(twosum(integers,target))


#method 3: hashmap approach
def twosum(nums,target):
    hashmap={}    #empty hashmap 
    for i in range(len(nums)):
        complement=target-nums[i]   #complement ka matlab hai ki target me se current number ko minus karne par jo bachta hai, usko complement kehte hain
        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[nums[i]]=i
integers=[1,2,3,4,5] #input argument
target=9            #input argument
print(twosum(integers,target))



#question 2
def checkpalindrome(name):
    left=0
    right=len(name)-1
    while left<right:
        if name[left]!=name[right]:
            return False
        left+=1
        right-=1
    return True

name=input("Enter a name: ") #input argument
if checkpalindrome(name):
    print(f"{name} is a palindrome.")
else:    print(f"{name} is not a palindrome.")

#question 3
def movezeros(nums):
    left=0   # left assign 0th index
    for right in range(len(nums)):  #right pointer start se end tak chalega
        if nums[right]!=0:   #jab right pointer zero se alag hoga, toh left aur right pointer ke elements swap karenge
            nums[left],nums[right]=nums[right],nums[left]  
            left+=1
    return nums
nums=[0,1,0,3,12] #input argument
print(movezeros(nums))    #function call    

#for right in range(len(nums)):
#   ^^^^^
#   Python automatically creates this variable
#   and assigns it values: 0, 1, 2, 3, 4...