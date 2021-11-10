from concurrent.futures import ThreadPoolExecutor

from Executor import Executor
from Reader import Reader


def main():
    reader = Reader()
    Executor.run_executor(reader.get_json(), ThreadPoolExecutor)


if __name__ == '__main__':
    main()
