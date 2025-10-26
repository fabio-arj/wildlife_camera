import easyocr
from files_extraction import extract_files
from frame_extraction import extract_frames
from typing import List, Any
import pandas as pd
from pathlib import Path

def run_ocr(path):
  file_list = extract_files(path)

  frame_list = extract_frames(file_list)

  reader = easyocr.Reader(['en','pt'])

  data_list = []
  for frame in frame_list:
    result: List[Any] = reader.readtext(frame[0][685:720, 900:1280])
    text = [r[1] for r in result]
    replaced = [text[0].replace(" ", ""), text[1].replace(" ", "")]
    final_list = [frame[1], replaced[0], replaced[1]]
    data_list.append(final_list)
    df = pd.DataFrame(data_list, columns=["id", "data", "hora"])
    df["data"] = pd.to_datetime(df["data"]).dt.strftime("%d/%m/%y")
    df["hora"] = pd.to_datetime(df["hora"]).dt.strftime("%H:%M:%S")
    df.sort_values(by=["data"])
  return df