#STUDENT: Jason Pettit
#CST205-40_SP19
#Module 6 Lab 13 Part 1 - Green eggs and ham

def eggs():
  setMediaPath()
  file = open(pickAFile())
  string = file.read()
  string = string.lower()
  string = string.split()
  file.close()
  
  words = {}
  
  #populate the dictionary with 
  #unique word:count of word
  for x in string:
    if x in words:
      words[x] += 1
    else:
      words[x] = 1
  
  keys = words.keys()
  values = words.values()
  
  print "Total number of words = " + str(len(words)) + "\n"
  print "Each of the " + str(len(words)) + " words appears in the story the following number of times:"
  
  #print the key:value pairs nicely formatted
  for y in range(0,len(keys)):
    print keys[y] + "\t\t" + str(values[y])
  
  storeCount = 0

  #find and store the most frequent word
  for y in range(0,len(keys)):
    if values[y] > storeCount:
      storeKey = keys[y]
      storeCount = values[y]
  
  print "The most frequent word is \"" + storeKey + "\" it occurs " + str(storeCount) + " times."

  
