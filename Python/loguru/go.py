# Installing  pip install loguru

from loguru import logger


def sample_1__to_console():
    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


def sample_2__to_file():
    logger.add("debug1.log", format="{time} {level} {message}", level="DEBUG")

    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


def sample_3__to_file_with_rotation():
    """
        After 10 kilobyte will be created new log file.
    :return:
    """
    logger.add("debug2.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB")

    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


def sample_3_1__to_file_with_rotation_by_week():
    """
        Каждую неделю будет пересоздаваться лог файл
    :return:
    """
    logger.add("debug3.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week")

    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


def sample_3_2__to_file_with_rotation_through_current_time():
    """
        Каждый день в десять утра будет создаваться новый log file

    :return:
    """
    #
    logger.add("debug4.log", format="{time} {level} {message}", level="DEBUG", rotation="10:00")

    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


def sample_4__to_file_with_rotation_and_compression():
    """
        After 10 kilobyte will be created new log file.
    :return:
    """
    logger.add("debug5.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip")

    for _ in range(1000):
        logger.debug("Hello, World (debug)!")


def sample_5__logging_to_json():
    """
        Логируем в JSON, очень удобно, для дальнейшего парсинга наших лог файлов, т.е. они будут доступны
        для автоматизированной обработки.
    :return:
    """
    logger.add("debug6.json", format="{time} {level} {message}", level="DEBUG", rotation="10:00", compression="zip", \
               serialize=True)

    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")


# декораторы

def divide(a, b):
    logger.add("debug7.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB")
    return a / b


@logger.catch
def main_1():
    divide(a, b)


@logger.catch
def main_2(a, b):
    divide(a, b)


if __name__ == '__main__':
    # 1.
    sample_1__to_console()

    # 2.
    #######################################
    sample_2__to_file()
    #######################################
    # debug1.log
    #######################################

    # Input

    # 2021 - 02 - 02T14: 59:25.197156 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T14: 59:25.197348 + 0300 INFO Hello, World(info)!
    # 2021 - 02 - 02 T14: 59:25.197531 + 0300 ERROR Hello, World(error)!

    #######################################

    # 3.
    #######################################
    sample_3__to_file_with_rotation()
    #######################################
    # debug2.log
    #######################################

    # Input

    # 2021 - 02 - 02 T15: 06:20.981484 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 06:20.981693 + 0300 INFO Hello, World(info)!
    # 2021 - 02 - 02 T15: 06:20.981829 + 0300 ERROR Hello, World(error)!
    #######################################

    # 4.
    #######################################
    sample_4__to_file_with_rotation_and_compression()
    #######################################
    # debug3.log
    # debug.2021 - 02 - 02_15 - 10 - 15_094732.log.zip
    # debug.2021 - 02 - 02_15 - 10 - 15_098806.log.zip
    # debug.2021 - 02 - 02_15 - 10 - 15_132846.log.zip
    # debug.2021 - 02 - 02_15 - 10 - 15_181527.log.zip
    # debug.2021 - 02 - 02_15 - 10 - 15_221387.log.zip
    # debug.2021 - 02 - 02_15 - 10 - 15_242495.log.zip

    #######################################

    # Input

    # 2021 - 02 - 02 T15: 10:15.263358 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264157 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264296 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264426 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264551 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264673 + 0300 DEBUG Hello, World(debug)!
    # 2021 - 02 - 02 T15: 10:15.264795 + 0300 DEBUG Hello, World(debug)!
    #######################################

    sample_3_1__to_file_with_rotation_by_week()

    sample_3_2__to_file_with_rotation_through_current_time()

    main_1()

    # Output
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # 2021 - 02 - 02 15: 32:09.141 | ERROR | __main__: < module >: 141 - Anerror has been caught in function
    # '<module>', process 'MainProcess'(22860), thread 'MainThread'(140619630995264):
    # Traceback(most recent call last):
    #
    # > File "go.py", line 141, in < module >
    # main()
    # └ < function main at 0x7fe48b6b3f28 >
    #
    # File "go.py", line 77, in main
    #     divide(a, b)
    #     └ < function divide at 0x7fe48b6b3e18 >
    #
    # NameError: name 'a' is not defined

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    main_2(1, 0)

    # Output
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #     2021 - 02 - 02 15: 35:56.575 | ERROR | __main__: < module >: 169 - An error has been caught in function
    #     '<module>', process 'MainProcess'(24125), thread 'MainThread'(139917609723712):
    #     Traceback(most recent call last):
    #
    #     > File "go.py", line 169, in < module >
    #         main_2(1, 0)
    #         └ < function main_2 at 0x7f4117b09268 >
    #
    #         File "go.py", line 82, in main_2
    #             divide(a, b)
    #             │      │  └ 0
    #             │      └ 1
    #             └ < function divide at 0x7f4117b0bd90 >
    #
    #         File "go.py", line 72, in divide
    #             return a / b
    #                     │  └ 0
    #                     └ 1
    #
    # ZeroDivisionError: division by zero

    # И всё это записалась в файл debug1.log
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    sample_5__logging_to_json()

    # Output
    # в формате JSON

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # {"text": "2021-02-02T15:49:30.314840+0300 DEBUG Hello, World (debug)!\n", "record": {"elapsed": {"repr": "0:00:00.009830", "seconds": 0.00983}, "exception": null, "extra": {}, "file": {"name": "go.py", "path": "go.py"}, "function": "sample_5__logging_to_json", "level": {"icon": "\ud83d\udc1e", "name": "DEBUG", "no": 10}, "line": 77, "message": "Hello, World (debug)!", "module": "go", "name": "__main__", "process": {"id": 29077, "name": "MainProcess"}, "thread": {"id": 140021196015424, "name": "MainThread"}, "time": {"repr": "2021-02-02 15:49:30.314840+03:00", "timestamp": 1612270170.31484}}}
    # {"text": "2021-02-02T15:49:30.315207+0300 INFO Hello, World (info)!\n", "record": {"elapsed": {"repr": "0:00:00.010197", "seconds": 0.010197}, "exception": null, "extra": {}, "file": {"name": "go.py", "path": "go.py"}, "function": "sample_5__logging_to_json", "level": {"icon": "\u2139\ufe0f", "name": "INFO", "no": 20}, "line": 78, "message": "Hello, World (info)!", "module": "go", "name": "__main__", "process": {"id": 29077, "name": "MainProcess"}, "thread": {"id": 140021196015424, "name": "MainThread"}, "time": {"repr": "2021-02-02 15:49:30.315207+03:00", "timestamp": 1612270170.315207}}}
    # {"text": "2021-02-02T15:49:30.315478+0300 ERROR Hello, World (error)!\n", "record": {"elapsed": {"repr": "0:00:00.010468", "seconds": 0.010468}, "exception": null, "extra": {}, "file": {"name": "go.py", "path": "go.py"}, "function": "sample_5__logging_to_json", "level": {"icon": "\u274c", "name": "ERROR", "no": 40}, "line": 79, "message": "Hello, World (error)!", "module": "go", "name": "__main__", "process": {"id": 29077, "name": "MainProcess"}, "thread": {"id": 140021196015424, "name": "MainThread"}, "time": {"repr": "2021-02-02 15:49:30.315478+03:00", "timestamp": 1612270170.315478}}}
