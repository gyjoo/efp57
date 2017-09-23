def isAnagram(string1, string2):
	'This function checks that whether strings are anagram or not'
	str1_size = len(string1)
	str2_size = len(string2)

	if str1_size != str2_size :
		print('Both input strings must be the same length.')
		return false
	
	for i in range(0,str1_size):
		for string1[i] in string2:
			return false
	
	return true

print("Enter two strings and I'll tell you if they are anagrams:")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = isAnagram(string1, string2)

if result:
	print("\"%s\" and \"%s\" are anagrams." %(string1,string2))
else:
	print("\"%s\" and \"%s\" are NOT anagrams." %(string1,string2))
