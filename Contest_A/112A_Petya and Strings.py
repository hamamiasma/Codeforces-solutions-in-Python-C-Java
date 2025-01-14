'''

Little Petya loves presents. His mum bought him two strings of the same size for his birthday. 
The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. 
The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. 
It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". 
If the second string is less than the first one, print "1". 
If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
'''






def compare_strings(str1, str2):
    # Convert both strings to lowercase (or uppercase) to make the comparison case-insensitive
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    
    # Compare the two strings lexicographically
    if str1_lower < str2_lower:
        return -1
    elif str1_lower > str2_lower:
        return 1
    else:
        return 0

# Read the input strings
string1 = input().strip()
string2 = input().strip()

# Perform the comparison and print the result
result = compare_strings(string1, string2)
print(result)