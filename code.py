import re

'''
num_of-occ function returning number of occurrences of the word to be searched
'''


def num_of_occ(search_word1, file_str1):
    occ = re.findall(search_word1, file_str1, re.M | re.I)  # returning list of the searched word
    l_occ = len(occ)
    return str(l_occ)


'''
list_lines function returns every line containing the search_word as an element in a new list variable
'''


def list_lines(file_str1):
    filter_search = []  # list of sentences containing the word to be searched
    l_file = file_str.split("\n")  # text file converted to list having elements line by line
    for i in range(len(l_file)):
        line = (l_file[i])  # taking elements as string for comparing with search_word in the next step
        if re.search(search_word, line, re.M | re.I):
            filter_search.append((line.split('\n')))  # the lines which contain the search_word gets appended into list
    return filter_search 


'''
function to get each element from the returning value from function list_lines, 
then iterate through it, find the next and previous words and append it to new file and then returning that file 
'''


def output_string(file_str_list1):
    for i in range(len(file_str_list1)):
        l_string = (" ".join(file_str_list1[i]))
        # l_string gets each sentence one by one which contains the search_word

        l_string_split = l_string.split(" ")
        # l_string converted to list having elements which are the sentence having the search_word

        # finding the index at which we have the search_word
        for j in range(len(l_string_split)):
            if re.search(search_word, l_string_split[j], re.M | re.I):
                
                if j == 0:  # if the search_word is at starting of the line take only next word
                    final_str = (l_string_split[j] + " " + l_string_split[j+1])
                    final_file.write(final_str + '\n')
                
                elif j == (len(l_string_split))-1:  # if the search_word is at ending of the line take previous word
                    final_str = (l_string_split[j-1] + " " + l_string_split[j])
                    final_file.write(final_str + '\n')                       
                
                else:  # if the search_word is in between of the line take previous as well as next word
                    final_str = (l_string_split[j-1] + " " + l_string_split[j] + " " + l_string_split[j+1]) 
                    final_file.write(final_str + '\n')
    return final_file                    
        

n = int(input("Enter number of words you want to search\n"))
for k in range(0, n):
    if __name__ == "__main__":
        new_file = open("input.txt", 'r')  # opened file and read it in a handler named new_file
        search_word = input("Enter word you want to search\n")
        final_file_name = search_word + '.txt'
        final_file = open(final_file_name, "a")
        file_str = new_file.read()  # input file converted to string and stored in a new variable named file_str
        final_file.write("Number of occurrences " + num_of_occ(search_word, file_str) + '\n')
        file_str_list = list_lines(file_str)
        final_output = output_string(file_str_list)

new_file.close()
final_file.close()
