print("loading...")
import os
import time
time.sleep(1)
import sys
import functions

#intro
os.system("clear")
print("Thanks for downloading filesys-terminal Pre-1. :) (also make a root folder. autosetup will be added into pre-2.)")
input("")
os.system("clear")

#define stuff
command = ""
commands = []

def error(input_):
    os.system("clear")
    
    print(input_)
    input("")

def restore():
        os.system("clear")
        
        for x in commands:
                print(x)

def fileExsists(input):
        if os.path.isFile(input):
                return(True)
        else:
                return(False)

def folderExsists(input):
        if os.path.exists(input):
                return(True)
        else:
                return(False)


def args(str_):
    args = []
    string_ = ""
    
    for x in  str_:
        if x == " ":
            args.append(string_)
            string_ = ""
        else:
            string_ = string_ + x
    args.append(string_)
    
    return(args)

while True:
        restore()
        command = input("")
        commands.append(command)
        
        args_ = args(command)
        
        if args_[0] == "exit":
         sys.exit()
        
        if args_[0] == "cdir":
         if len(args_) == 2:
          if folderExsists("root/" + args_[1]) == False:
             os.mkdir("root/" + args_[1])
          else:
              error("folder already exsits.")
         else:
             error("cdir takes 2 arguments, not " + str(len(args_)) + "!")
        
        if args_[0] == "clear":
            commands = []
        
        if args_[0] == "rmdir":
            if len(args_) == 2:
                if folderExsists("root/" + args_[1]):
                   functions.cleanDir("root/" + args_[1])
                   os.rmdir("root/" + args_[1])
                else:
                    error("folder does not exsist.")
            else:
                 error("rmdir takes 2 arguments, not " + str(len(args_)) + "!")
        
        
        # comment :D

os.system("clear")
