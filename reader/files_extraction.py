import os

def extract_files(path):
  path_list = []
  for (dirpath, _, filename) in os.walk(path): 
      for files in filename:
        path_list.append(os.path.join(dirpath, files))
  return path_list