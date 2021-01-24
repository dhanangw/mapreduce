import multiprocessing
from typing import Any, Callable, Dict, List


class Reducer:
    @classmethod
    def reduce(
        cls,
        reducer_function: Callable[[Any], Any],
        argument: List[Dict[str, Any]],
        num_of_worker: int = 3
    ) -> Any:
        with multiprocessing.Pool(processes=num_of_worker) as pool:
            result = pool.apply_async(reducer_function, (argument,)).get()
            pool.close()
            pool.join()
        return result

        