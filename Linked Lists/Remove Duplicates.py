# Remove Duplicates from Sorted List
class Solution:
    def deleteDuplicates(self, head):
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
sol = Solution()
print(sol.deleteDuplicates([1,1,2])) #[1,2]