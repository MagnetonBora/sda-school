from collections import defaultdict


def find_index(collection, target):
    for idx, item in enumerate(collection):
        if item == target:
            return idx
    return -1


def max_score(collection):
    return max([item[-1] for item in collection])


def min_score(collection):
    return min([item[-1] for item in collection])


def avg_score(collection):
    scores = [float(item[-1]) for item in collection]
    return sum(scores) / len(collection)


def score_stats(collection):
    stats_dict = defaultdict(list)
    for elem in collection:
        score = elem[-1]
        stats_dict[score].append(elem)
    return stats_dict
