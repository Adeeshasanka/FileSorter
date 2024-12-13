import os
import shutil

folder = input(str("folder location: "))
contents = os.listdir(folder)
py_files = []
html_files = []
txt_files = []
pdf_files = []
file_types = {}

def file_sort(extension):
   print("got it!")



while True:
  print("\n")
  print("Select the extension or command.")
  print("1.py   : python files ")
  print("2.html : html files")
  print("3.txt  : text files")
  print("4.pdf  : pdf files")
  print("5.d    : to view FileTypes dictionary")
  print("6.exit : to exit the folder")

  extension = input(str("Enter your file extension: "))

  if (extension in ("py","html","txt","pdf")):
     file_sort(extension)
  elif (extension == "d"):
      print(file_types)
  elif (extension == "exit"):
      print("\nFolder was closed...\n")
      with open("C:\\Users\\X512\\Desktop\\python course\\Filesort_app\\Main.py") as f:
          exec(f.read())
  elif not extension in ("py", "html", "txt", "pdf", "d", "exit"):
     print("\nEnter a valid extension")
