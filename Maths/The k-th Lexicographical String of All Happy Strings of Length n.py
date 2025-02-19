import math


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        '''Approach: Maths. The problem asks to find the kth lexicographical string
        of all happy strings of length n. A happy string contains only the letters
        a, b and c and two neighbours can never be the same. So given n the length
        of the string and k to find the kth string when we can sort the generated
        strings in lexicographical order. The brute force approach would be to
        generate each and every string and then sort it to find the kth. But this
        approach has a time complexity of exponential. So can we optimize it? Yes
        Let us see how. Here we are thinking about ordering a string that can start
        with 3 letters which means if the answer exists it will start by one of these
        letters and since we will be sorting it, it would be a then b then c now if
        there is one possibility for the first letter then for each positions that
        are remaining there would be 2 choices giving us 2**(n-1) number of strings
        for each letter. This means the first 2**(n-1) strings start with a then with
        b and it continues. So now we need to find on which interval does the current
        k lies after identifying that we need to remove any previous unnecessary counts
        for the next calculation.'''
        letters = ['a','b','c']

        #a function to get the character identified by the index
        def getCharacter(index,removed_char):
            counter = 1
            for i in range(3):
                if letters[i] == removed_char: #if the letter has been previously used skip it
                    continue
                if counter == index:
                    return letters[i]
                counter += 1
            return letters[-1]

        answer = []
        total_possibility = math.pow(2,n-1) #calculating the total possibility ignoring the first position
        prev = "" #for holding the previous character to avoid repetition of letters
        for i in range(n):
            index = math.ceil(k/total_possibility) #calculate where the index will lie it's either 1 or 2 or 3
            
            if index > 3: #handle the case when it's greater than 3 as the string doesn't exist
                return ""

            cur_letter = getCharacter(index,prev)
            answer.append(cur_letter)
            prev = cur_letter
            k -= ((index-1)*total_possibility) #remove the previous count
            total_possibility //= 2
        
        
        return "".join(answer)
        #Time Complexity: O(3*n)
        #Space Complexity: O(n) and since n is max 10 we can say both the time and space complexity are constant
