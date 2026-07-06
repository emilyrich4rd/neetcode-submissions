class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        currProduct = 1
        for i in range(len(nums)):
            out[i] = currProduct
            currProduct *= nums[i]
        suffixProd = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= suffixProd
            suffixProd *= nums[i]
        return out
        

        