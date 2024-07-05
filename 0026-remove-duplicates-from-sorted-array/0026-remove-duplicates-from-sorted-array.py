class Solution(object):
    def removeDuplicates(self, nums):
        # In python, if the str, list and etc is empty, it will return a False.
        # Therefore by introducing if not, it will be if nums is True (empty)
        # Then the following action is return 0
        if not nums:
            return 0


        # Count for unique value
        k = 1
        # For m, starting from index (1), to the remaining length of the nums
        for m in range(1,(len(nums))):
            # If the second index nums does not == the k nums
            if nums[m-1] != nums[m]:
                # Since the unique count is added, we want to update the new value of k
                # therefore the k value is replace by the updated value
                nums[k] = nums[m]
                # Unique count += 1 
                k+=1
        # It cannot be put inside the loop because it will end the loop premature because there is a return K
        # Therefore one the loop is finish, only the return K can provide the accurate count of unique value
        return k


        
            

        