import multiprocessing
def wrapped_function(target_function, queue):
    result = target_function()
    queue.put(result)

def run_with_timeout(target_function, timeout):
    result_queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=wrapped_function, args=(target_function, result_queue))
    process.start()
    process.join(timeout)

    if process.is_alive():
        print(f"Program timed out after {timeout} seconds. Terminating process...")
        process.terminate()
        process.join()
        print("Process terminated.")
        # return None if being terminated
        return None
    else:
        print("The program completed within the specified time.")
        if not result_queue.empty():
            return result_queue.get()
        else:
            return None
