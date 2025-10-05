#WordCount.py
#Name: Grant Schaeffer
#Date: 10/4/25
#Assignment: Word Count

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letter = line.split()
    for char in textFile:
        if char.isalpha():
          letterCount += 1
    #print(line)
  
  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Letters: ", letterCount)

if __name__ == '__main__':
  main()
