import re

new_file= open("D:\AMAN\mini_project\input.txt", 'r') # opened file and read it in a handler named new_file
final_file = open("D:\AMAN\mini_project\output.txt","a") #creating a new text file to store the output 

filter_search=[] #list of sentences conatining the word to be searched
uni= []
file_str= new_file.read() #input file converted to string and stored in a new variable named file_str

search_word= input("enter word you want to search\n") #taken input for the word to be searched
occ= re.findall(search_word, file_str, re.M|re.I) #regx
l_occ= len(occ)
final_file.write("Number or occurences " +str(l_occ)+ '\n')

l_file= file_str.split("\n") #text file converted to list by chnaging lines

#to get every line containing the search_word as an element in a new list variable
for i in range(len(l_file)):
    line= (l_file[i]) #taking elements as string for comparing with search_word in the next step  
    if re.search(search_word, line, re.M|re.I):
        filter_search.append((line.split('\n'))) #the lines which contain the search_word gets appended in this list



for i in range(len(filter_search)):
    l_string=(" ".join(filter_search[i])) #l_string gets each sentence one by one which contains the search_word
    l_string_split = l_string.split(" ")  #l_string converted to list having elements as the strings in the sentence having the search_word

    #finding the index at which we have the search_word
    for j in range(len(l_string_split)):
        if re.search(search_word, l_string_split[j], re.M|re.I):
            if j== 0:                                                    #if the search_word is at starting of the line take only next word
                final_str= (l_string_split[j]+ " "+ l_string_split[j+1])
                final_file.write(final_str+ '\n')
            elif j== (len(l_string_split))-1:                            #if the search_word is at ending of the line take only previous word
                final_str= (l_string_split[j-1]+ " "+ l_string_split[j])
                final_file.write(final_str + '\n')                       
            else:                                                        #if the search_word is in betweeen of the line take previous as well as next word
                final_str= (l_string_split[j-1]+ " " +l_string_split[j] + " " +l_string_split[j+1]) 
                final_file.write(final_str+ '\n')

new_file.close()
final_file.close()