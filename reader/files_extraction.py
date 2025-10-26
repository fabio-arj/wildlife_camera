import os

def extract_files(path):
  path_list = []
  for (dirpath, _, filename) in os.walk(path): 
      for files in filename:
        r_text = files.split(".")
        path_list.append([os.path.join(dirpath, files), r_text[0]])
  return path_list