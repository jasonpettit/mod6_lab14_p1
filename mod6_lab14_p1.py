def eggs():
  setMediaPath()
  file = open(pickAFile())
  string = file.read()
  string = string.lower()
  string = string.split()
  
  words = []
  
  for x in range(0,len(string)):
    if string[x] not in words:
      words.append(string[x])
  
  words.sort()
  
  numWords = len(words)
  print "Total number of words = " + str(numWords)