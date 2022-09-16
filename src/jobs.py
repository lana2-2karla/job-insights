import csv
from functools import lru_cache


@lru_cache
def read(path: str):
    with open(path, mode="r") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs)
