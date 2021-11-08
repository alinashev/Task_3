import time

from Counter import Counter


class Executor():
    def run_executor(json_string, executor_class):
        executor = executor_class(max_workers=2)
        start_time_thread = time.time()
        fututres_1 = executor.submit(Counter.counting,
                                     json_string=json_string,
                                     start_value=0,
                                     end_value=int(len(json_string['questions']) / 2))
        fututres_2 = executor.submit(Counter.counting,
                                     json_string=json_string,
                                     start_value=int(len(json_string['questions']) / 2),
                                     end_value=len(json_string['questions']))

        result = fututres_2.result() + fututres_1.result()
        print("Results:{result}. Executor:{executor}. Time:{spent_time}".format(
            result=result,
            executor=executor_class.__name__,
            spent_time=time.time() - start_time_thread
        ))
