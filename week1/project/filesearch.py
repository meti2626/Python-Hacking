import os

def find_txt_files(directory):
  #
  print(f"Searching for .txt files in: {directory}")


  for root , dirs , files in os.walk(directory):
       
       for file in files:
           if file.endswith(".txt"):
               print(os.path.basename(file))

if __name__ == "__main__":
  
  path = input("Enter the flder path to search :")

if os.path.isdir(path):
    find_txt_files(path)

else:
    
    print("The provided path is not a valid directory.")