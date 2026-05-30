import basic
import sys

def run_repl():
   while True:
      text = input("basic >>")

      if text.lower() == "exit":
        break
     
      if text == "":
        continue


      result , error = basic.run("<stdin>",text)
    
      if error:
          print(error.as_string())
      if result is not None :
        print(result) 


def run_file(filename) :
   try:
      with open (filename , "r") as f :
         text = f.read()
      result , error = basic.run(filename, text)   

      if error:
          print(error.as_string())
      if result is not None:
        print(result) 
   except FileNotFoundError :
      print(f"filname {filename} is not  found")

if __name__ =="__main__":
   if len(sys.argv) > 1 :
      run_file(sys.argv[1])
   else :
      run_repl()   

