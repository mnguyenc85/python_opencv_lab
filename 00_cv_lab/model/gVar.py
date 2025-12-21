from model.pipeline_node import CPipelineNode

global_pipline_id : int = 0
global_pipeline_cache = { }

def add_cache(o: CPipelineNode) -> int:
  global global_pipline_id
  global_pipline_id += 1
  global_pipeline_cache[global_pipline_id] = o
  return global_pipline_id