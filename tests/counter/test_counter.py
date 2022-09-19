from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "javaScript"
    count = 122

    assert count_ocurrences(path, word) == count
