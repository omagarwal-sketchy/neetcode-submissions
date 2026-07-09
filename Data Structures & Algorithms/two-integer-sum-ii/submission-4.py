class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target-numbers[i] in set(numbers[i+1:len(numbers)]):
                break
        for j in range(i+1,len(numbers)):
            if numbers[j]==target-numbers[i]:
                break
        return[i+1,j+1]