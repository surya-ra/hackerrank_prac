class LinkedList:
    def __init__(self, x, idx):
        self.val = x
        self.index = idx
        self.next = None

class Solution:
    def append(self, item, search):
        head_ptr = LinkedList(0, 0)
        cur_ptr = head_ptr
        indx = 0
        final_len = 0
        for nums in item:
            indx += 1
            cur_ptr.next = LinkedList(nums, indx)
            cur_ptr = cur_ptr.next
            final_len = indx
        cur_ptr = head_ptr.next
        final_len = final_len
        #print(final_len)
        result = self.findIndex(search, final_len, cur_ptr)
        return result

    def findIndex(self, search, total_length, l_list):
        search_index = (total_length - search) + 1
        a = 'NIL'
        if search_index <= 0:
            return a
        while l_list.next != None:
            if l_list.index == search_index:
                return l_list.val
            else:
                l_list = l_list.next
        if l_list:
            if l_list.index == search_index:
                return l_list.val

        

#n = int(input())
#ls = list(map(int,input().strip().split()))
n = 1
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SolutionObj = Solution()
print (SolutionObj.append(ls, n))

