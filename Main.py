import os       #allows me to acces files and folders
import shutil   #particularly useful for tasks involving file copying, moving, renaming, and removal, as well as handling directories.

folder = input(str("folder location: "))
contents = os.listdir(folder)
py_files = []
html_files = []
txt_files = []
pdf_files = []
file_types = {}

def file_sort(extension):
   
    if (extension == "py"):
      for item in contents:
         if item.endswith(".py"):
            py_files.append(item)
      print(py_files)

    elif (extension == "txt"):
      print("text files!")

    elif (extension == "pdf"):
       print("pdf files!")

    elif (extension == "html"):
       print("HTML files!")



#keeps the programme running to let user input again
while True:
  
  #to let the user know about the programme
  print("\n") 
  print("Select the extension or command.")
  print("1.py   : python files ")
  print("2.html : html files")
  print("3.txt  : text files")
  print("4.pdf  : pdf files")
  print("5.d    : to view FileTypes dictionary")
  print("6.exit : to exit the folder")

  extension = input(str("Enter your file extension: "))  #taking the user input

  if (extension in ("py","html","txt","pdf")):    #checking if its a valid exxtention
     file_sort(extension)
  elif (extension == "d"):     
      print(file_types)            #prints the file_types dict
  elif (extension == "exit"):
      print("\nFolder was closed...\n")
      #opens the file again so the user can have a fresh start!
      with open("C:\\Users\\X512\\Desktop\\python course\\Filesort_app\\Main.py") as f:   
          exec(f.read())
  elif not extension in ("py", "html", "txt", "pdf", "d", "exit"):
     print("\nEnter a valid extension")
