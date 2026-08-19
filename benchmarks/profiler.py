"""
Performance & Memory Profiling Harness for Refactoring Benchmarks.
"""
import time
import tracemalloc
from typing import Callable, Any, Dict

def profile_execution(func: Callable[..., Any], *args, **kwargs) -> Dict[str, Any]:
    """
    Measures execution time and peak memory footprint of a target function.
    """
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = func(*args, **kwargs)
    
    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        "result": result,
        "elapsed_ms": round(elapsed_ms, 3),
        "peak_memory_mb": round(peak_mem / (1024 * 1024), 4)
    }
