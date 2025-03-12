from .model import Model
from events import raise_event
import duckdb


def sql(model: Model, query: list[str]) -> None:
    print(query)
    tables = []
    start = 0
    stop = len(query)+1
    for i, token in enumerate(query):
        if token.lower() == 'from':
            start = i+1
        if token.lower() == 'where':
            stop = i

    print(start, stop)
    print(query[start:stop])
