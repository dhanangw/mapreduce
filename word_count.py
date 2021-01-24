import argparse
import os
from typing import Any, Dict, List

from map import Mapper
from reduce import Reducer


def mapper_function(filepath: str) -> int:
    word_count = 0
    with open(filepath, 'r') as text_file:
        data = text_file.read()
        word_count = data.split()
    return len(word_count)

def reducer_function(count_results: List[Dict[str, Any]]) -> int:
    total_word_count = 0
    for count in count_results:
        total_word_count += count["value"]
    return total_word_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="relative path from project's root to directory of TXT file")
    args = parser.parse_args()

    input_txt_path = args.input_dir
    filenames = os.listdir(input_txt_path)
    current_path = os.path.abspath(os.getcwd())
    inputs = [os.path.join(current_path, f"{input_txt_path}/{filename}") for filename in filenames]
    map_results = Mapper.map(
        mapper_function=mapper_function,
        arguments=inputs
    )
    reduce_result = Reducer.reduce(reducer_function, map_results)
    print(reduce_result)
