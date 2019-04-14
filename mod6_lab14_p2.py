#STUDENT: Jason Pettit
#CST205-40_SP19
#Module 6 Lab 14 Part 2 - Headlines

def headlines():
  setMediaPath()
  file = open(pickAFile(),"r")
  
  startString = "uscb-margin-TB-02 uscb-title-3"
  line = ''
  
  print "U.S. Census Bureau Headlines"
  
  for headline in file:
    if startString in line:
      print headline
    line = headline
    
  
  

  