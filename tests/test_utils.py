import sys
from io import StringIO
from contextlib import contextmanager


@contextmanager
def captured_output():
    stdout = sys.stdout
    out = StringIO()
    try:
        sys.stdout = out
        yield sys.stdout
    finally:
        sys.stdout = stdout