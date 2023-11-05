# Solomon Falode 2154980
# Read a list of words from the user
words=input().split(' ')

#using the for loop Count the frequencies of each word
for ws in words:
    word_frequency=0
    frq=0 
    #using the for loop 
    while frq<len(words):
        #checking the word 
        if ws==words[frq]:
            word_frequency+=1 #this will increment the frequency count 

        frq=frq+1 #increment the value of frq

    #print the word and frequency count 
    print(ws+"",word_frequency)
