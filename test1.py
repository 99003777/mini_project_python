import re

new_file= open("D:\AMAN\mini_project\input.txt", 'r')# opened file and read it in a handler

filter_search=[]
uni= []
file_str= new_file.read() #converted to string
search_word= input("enter word you want to search") #taken input for the word to be searched
occ= re.findall(search_word, file_str, re.M|re.I) #regx
print(len(occ))
l_file= file_str.split("\n") #text file converted to list by chnaging lines
for i in range(len(l_file)):
    line= (l_file[i]) #taking elements as string for comparing with search_word in the next step  
    if re.search(search_word, line, re.M|re.I):
        filter_search.append((line.split('\n'))) #the lines which contain the search_word gets appended in this list
print(filter_search)

for i in range(len(filter_search)):
    l_string=(" ".join(filter_search[i]))
    l_string_split = l_string.split(" ")
    '''
    for j in range(len(l_string_split)):
        if re.search(search_word, l_string_split[j], re.M|re.I):
            #print(l_string_split[j-1]+ " " +l_string_split[j] + " " +l_string_split[j+1])
    '''
