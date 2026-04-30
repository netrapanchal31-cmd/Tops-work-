#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
#'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.  
#Return the resulting string

word=input("enter a statement ")
new_word=""
new_word=word.replace("not poor","good")
print(new_word)
