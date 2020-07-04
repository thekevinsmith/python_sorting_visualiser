import sys
import os
import pytest


def run():
    print("RUN")
    pass


def test():
    print("TEST")
    print(os.getcwd())
    pytest.main()


if __name__ == "__main__":

    function_map: dict = dict(
        run=run,
        test=test
    )
    print(os.getcwd())
    function_map[sys.argv[1]]()
