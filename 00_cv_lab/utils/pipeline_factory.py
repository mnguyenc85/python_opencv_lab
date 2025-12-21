import cv2
import model.gVar as gVar
from model.pipeline_node import CPipelineNode

def create_loadimage_node(file_path: str) -> CPipelineNode:
  try:
    img = cv2.imread(file_path)

    pl = CPipelineNode()
    pl.action = 10000                   # load image file
    pl.output = img
    pl.id = gVar.add_cache(pl)

    return pl

  except Exception as e:
    print(e)