import time
import random
bruh=0
bruh2=0
#--------------------------------------------------------------------------------------------------
#First Mode
def mode1():
 bruh=0
 bruh2=0
 time.sleep(0.2)
 print("Bruh Checkpoint Bottom Random Number?")
 botint=int(input())
 time.sleep(0.2)
 print("Bruh Checkpoint Top Random Number")
 topint=int(input())
 time.sleep(0.2)
 while True:
  intv2 = random.randint(botint,topint)
  bruh2=0
  print("Bruh Checkpoint:")
  time.sleep(0.2)
  print("You Have Witnessed")
  time.sleep(0.2)
  print(bruh) 
  time.sleep(0.2)
  print("bruhs.") 
  while True:
   time.sleep(0.01)
   print("bruh")
   print("----")
   bruh=bruh+1
   bruh2=bruh2+1
   if intv2 == bruh2:
    break
#--------------------------------------------------------------------------------------------------
#Second Mode
def mode2():
 bruh=0
 bruh2=0
 intv=10
 time.sleep(0.2)
 print("Bruh Checkpoint Interval?")
 intv=int(input())
 time.sleep(0.2)
 while True:
  bruh2=0
  print("Bruh Checkpoint:")
  time.sleep(0.2)
  print("You Have Witnessed")
  time.sleep(0.2)
  print(bruh) 
  time.sleep(0.2)
  print("bruhs.")
  
  while True:
   time.sleep(0.01)
   print("bruh")
   print("----")
   bruh=bruh+1
   bruh2=bruh2+1
   if intv == bruh2:
    break
#-----------------------------------------------------------------------------------------------------
#Third Mode
def mode3():
 time.sleep(0.2)
 while True:
  time.sleep(0.01)
  print("bruh")
  time.sleep(0.01)
  print("----")
#------------------------------------------------------------------------------------------------
#Choose Bruh Mode
print("Welcome! Would you like")
time.sleep(0.2)
print("1)Random Interval Bruh Checkpoints")
time.sleep(0.2)
print("or")
time.sleep(0.2)
print("2)Set Interval Bruh Checkpoints")
time.sleep(0.2)
print("or")
time.sleep(0.2)
print("3)No Bruh Checkpoints")
mode=input("")
#----------------------------------------------------------------------------------------------------------
#Calling Upon Functions
if mode=='1':
 mode1()
elif mode=='2':
 mode2()
elif mode=='3':
 mode3()
#--------------------------------------------------------------------------------------------------
