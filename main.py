import basic
print("started")

def run_repl():
   print("repl is running")
   print("type is exit to quite")
   while True:
      text = input("basic >>")

      if text.lower() == "exit":
        break
     
      if text == "":
        continue


      result , error = basic.run("<stdin>",text)
    
      if error:
          print(error.as_string())
      else:
        print(result) 


run_repl()

 


        
    