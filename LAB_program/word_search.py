import sys
cout=0
w=input("Entr the word to search\n")
with open('word_search.txt','r') as f:
    for i in f:
        word=i.split()
        print(word)
        for words in word:
            if(words==w or words.upper()==w or words.lower()==w):
                print("Match found")
                sys.exit()
                cout+=1
if(cout==0):
 print( "Match not found")

