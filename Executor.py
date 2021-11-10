import time

from Counter import Counter


class Executor():
    def run_executor(json_string, executor_class):
        executor = executor_class()
        start_time_thread = time.time()
        half = int(len(json_string['questions']) / 2)

        result = 0
        inter = [0, int(len(json_string['questions']) / 2), len(json_string['questions'])]
        for i in range(0, len(inter) - 1):
            futures = executor.submit(Counter.counting,
                                      json_string=json_string,
                                      start_value=inter[i],
                                      end_value=inter[i + 1])
            result += futures.result()

        spent_time = time.time() - start_time_thread
        print("Results:{result}. Executor:{executor}. Time:{spent_time}".format(
            result=result,
            executor=executor_class.__name__,
            spent_time=spent_time
        ))
