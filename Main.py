import os       #allows me to acces files and folders
import shutil   #particularly useful for tasks involving file copying, moving, renaming, and removal, as well as handling directories.

folder_path = input(str("folder location: "))
contents = os.listdir(folder_path)

if folder_path != None:
   folder_path = r"{}".format(folder_path)

py_file_paths = []
py_files = []
html_file_paths = []
html_files = []
txt_file_paths = []
txt_files =[]
pdf_file_paths = []
pdf_files = []
file_types = {}

def file_sort(extension):
   
    if (extension == "py"):                                                       #checks the extension
      no_of_py_files = 0                                                          #declare local variable to keep track of number of files
      for item in contents:
         if item.endswith(".py"):                                                 #see if file ends with .py
            file_path = os.path.join("{}\\{}").format(folder_path, item)          #saves the path for the python file as a variable
            py_file_paths.append(file_path) 
            py_files.append(item)  
            no_of_py_files += 1
      #print(py_files)
      print("\nThere are {} python files in the folder".format(no_of_py_files))   #prints out the number of py files found
      file_types["Number of python files"] = no_of_py_files                       #adds the number of py files to the dictionary

      if py_files != None:
         i = 0
         new_folder_path = os.path.join(folder_path, "Py_files")                  #stores the path of the new folder that to be created as a variable
         #print(new_folder_path)
         os.makedirs(new_folder_path, exist_ok=True)                              #creates a new folder to store py files
         for py_file in py_files:
            destination_path = os.path.join(new_folder_path, py_file)
            if os.path.exists(destination_path):
               print("{}| File already exists!".format(py_file))
            else:
               shutil.copyfile(py_file_paths[i], destination_path)                   #copy paste each python file to desired destination
            i = i + 1                                         

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

  if (extension in ("py","html","txt","pdf")):           #checking if its a valid exxtention
     file_sort(extension)
  elif (extension == "d"):     
      print(file_types)                                  #prints the file_types dict
  elif (extension == "exit"):
      print("\nFolder was closed...\n")
      #opens the file again so the user can have a fresh start!
      with open("C:\\Users\\X512\\Desktop\\python course\\Filesort_app\\Main.py") as f:   
          exec(f.read())
  elif not extension in ("py", "html", "txt", "pdf", "d", "exit"):
     print("\nEnter a valid extension")
