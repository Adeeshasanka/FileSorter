import os       #allows me to acces files and folders
import shutil   #particularly useful for tasks involving file copying, moving, renaming, and removal, as well as handling directories.

folder_path = input(str("folder location: "))
contents = os.listdir(folder_path)

if folder_path != None:
   folder_path = r"{}".format(folder_path)

Should_Delete = None

#initialize the dictionary
file_types = {}

def file_sort(extension, folder_name):
    """
    Sort files of a specific extension into a designated folder.
    
    Parameters:
    extension (str): File extension to sort (e.g., "py", "txt").
    folder_name (str): Name of the folder where files will be moved.
    """
    # Initialize variables
    files = []
    file_paths = []
    no_of_files = 0

    # Find all files with the given extension
    for item in contents:
        if item.endswith(f".{extension}"):  # Check for matching extension
            file_path = os.path.join(folder_path, item) #the path of the file
            file_paths.append(file_path)
            files.append(item)
            no_of_files += 1

    print(f"\nThere are {no_of_files} {extension} files in the folder.")  # Print the number of files found
    file_types[f"Number of {extension} files"] = no_of_files  # Update dictionary with file count

    # Create a folder for the files
    if files:
        i = 0
        new_folder_path = os.path.join(folder_path, f"{extension}_Files")
        os.makedirs(new_folder_path, exist_ok=True)

        # Copy files to the new folder
        for file in files:
            destination_path = os.path.join(new_folder_path, file)
            if os.path.exists(destination_path):
                print(f"{file}| File already exists!")
            else:
                shutil.copyfile(file_paths[i], destination_path)
            i += 1

    # Delete files if required
    if Should_Delete == "y":
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)

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
     Should_Delete = input(str("\nDo you also want to delete the original files after copying? [type 'y' or 'n']"))
     file_sort(extension, folder_path)
  elif (extension == "d"):     
      print(file_types)                                  #prints the file_types dict
  elif (extension == "exit"):
      print("\nFolder was closed...\n")
      #opens the file again so the user can have a fresh start!
      with open("C:\\Users\\X512\\Desktop\\python course\\Filesort_app\\Main.py") as f:   
          exec(f.read())
  elif not extension in ("py", "html", "txt", "pdf", "d", "exit"):
     print("\nEnter a valid extension")
  elif not Should_Delete in ("y", "n"):
     print("\nEnter 'y' or 'n' only")
