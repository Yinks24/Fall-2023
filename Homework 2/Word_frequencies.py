#solomon falode 2154980
import csv


def main():
  
  #Prompt the input filename from the user.
  input_filename = input()

  #Open the input file
  file = open(input_filename)

  #Declare a "word_counts" to create a
  #CSV reader object to read the file.
  word_counts = csv.reader(file, delimiter=',')

  words = []

  #Start a for loop to iterate through each
  #row in the CSV file.
  for row in word_counts:
    #Start a for loop to iterate through each
    #word in the row and strip
    #any extra whitespace.
    for word in row:
      words.append(word.strip())

  #Start a for loop through the list of words.
  for i in range(len(words)):
    # Check if the current word is not
    #seen before in the previous words
    if words[i] not in words[:i]:

      count = 0

      #Start a for loop to count the occurrences
      #of the current word in the entire list.
      for w in words:
        if words[i] == w:
          count += 1
      #Print the word and its count
      print(words[i], count)

  #Close the input file
  file.close()

#Execute the main() function. 
if __name__ == "__main__":
  main()