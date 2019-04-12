#STUDENT: Jason Pettit
#CST205-40_SP19
#Module 6 Lab 13 Part 2 - Headlines

def headlines():
  setMediaPath()
  file = open(pickAFile(),"rt")
  string = file.read()
  file.close()
  
  headlines = []
  
  start = "<p class=\"uscb-margin-TB-02 uscb-title-3\">"
  end = "</p>"
  
  #print start
  
  print string.find(start)
  
  #for start in string:
    #print start
  
    
    
  
