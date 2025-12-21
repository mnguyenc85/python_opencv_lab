import numpy as np

class CPipelineNode:
  def __init__(self):
    self.id = 0
    self.output = None
    self.action = None