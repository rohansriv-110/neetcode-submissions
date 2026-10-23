class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # If the character is already in our set, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            # Add the new character to the window set
            char_set.add(s[r])
            
            # Update the maximum length found so far
            max_len = max(max_len, r - l + 1)
            
        return max_len

# --- Example Usage ---
sol = Solution()

s1 = "zxyzxyz"
print(f"Input: '{s1}' -> Longest Length: {sol.lengthOfLongestSubstring(s1)}") 
# Output: 3 ("xyz")

s2 = "xxxx"
print(f"Input: '{s2}' -> Longest Length: {sol.lengthOfLongestSubstring(s2)}") 
# Output: 1 ("x")