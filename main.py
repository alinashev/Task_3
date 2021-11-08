from concurrent.futures import ProcessPoolExecutor

from Executor import Executor
from Reader import Reader


def main():
    reader = Reader('res/osmi.json')
    Executor.run_executor(reader.get_json(), ProcessPoolExecutor)


if __name__ == '__main__':
    main()