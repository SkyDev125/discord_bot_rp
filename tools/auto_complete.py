import difflib


def fuzzysearch(item, list, n=1, cutoff=0.1):
    return difflib.get_close_matches(item, list, n, cutoff)
