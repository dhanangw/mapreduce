import multiprocessing
from typing import Any, Callable, Dict, List


class Mapper:
    @classmethod
    def map(
        cls,
        mapper_function: Callable[[Any], Dict[str, Any]], 
        arguments: List[Any],
        num_of_worker: int = 3
    ) -> List[Dict[str, Any]]:
        results = []
        with multiprocessing.Pool(processes=num_of_worker) as pool:
            for argument in arguments:
                results.append(pool.apply_async(mapper_function, (argument,)).get())
            pool.close()
            pool.join()
        return results
