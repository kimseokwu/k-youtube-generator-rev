from typing import Callable, List
from functools import reduce

def make_pipeline(function_list: List[Callable]) -> Callable:
    def pipeline(input):
        execute_pipeline = lambda func, x: func(x)
        output = reduce(execute_pipeline, function_list, input)
        return output
    return pipeline

