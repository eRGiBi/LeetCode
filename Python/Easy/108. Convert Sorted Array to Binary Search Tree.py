def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        total_nums = len(nums)
        if not total_nums:
            return None

        mid = total_nums // 2

        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))

