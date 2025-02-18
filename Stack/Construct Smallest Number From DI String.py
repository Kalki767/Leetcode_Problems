class Solution:
    def smallestNumber(self, pattern: str) -> str:
        '''Approach: Stack. The problem asks to find the lexicographically smallest
        string that contain unique digits and will fulfill the requirement on the
        pattern string. Here to solve this we can do the brute force which is generating
        each and every combination and checking if it satisfies the condition. But
        this approach is inefficient. For that case let's do some observation. Here
        we know that if the current character in the pattern is I then it means the
        next element need to be greater than it. So we need to take the minimum possible
        from what we have if we are being greedy we can sort the elements and take
        the first that hasn't been taken and put it in the answer. But what if we have
        a D then that means the next element need to be lesser. For that case we need
        to know how many consecutive D's we have together. Instead of putting the smallest
        we have we will be needing the reverse order of what we can put if it was an I
        For that case we can push the value to the stack and pop everything out when
        we come to the increasing one. Otherwise we need to pop them out at the end.'''
        counter = 2
        stack = [str(1)]
        answer = []
        for i in pattern:
            if i == 'I': #if the character is I pop everything out and place them in the answer
                while stack:
                    answer.append(stack.pop())
            stack.append(str(counter)) #simply append the next value
            counter += 1

        while stack:
            answer.append(stack.pop())

        return "".join(answer)
        #Time Complexity: O(n)
        #Space Complexity: O(n) where n is the length of the pattern