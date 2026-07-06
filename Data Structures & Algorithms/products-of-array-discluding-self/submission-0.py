class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        currProduct = 1
        out[0] = currProduct
        for i in range(1, len(nums)):
            currProduct *= nums[i-1]
            out[i] = currProduct
        suffixProd = 1
        for i in range(len(nums)-2, -1, -1):
            suffixProd *= nums[i+1]
            out[i] *= suffixProd
        return out
        

        