from decord import VideoReader
from decord import cpu

def extract_frames(path_list):
  frames_list = []
  for path in path_list:
    vr = VideoReader(str(path), ctx=cpu(0))
    frames_list.append(vr[0].asnumpy())
  return frames_list