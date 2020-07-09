from typing import List

def  h_index(citations: List[int]):
    m = map(min, enumerate(sorted(citations, reverse=True), 1))

    print(list((sorted(citations, reverse=True), 1)))
    #return max(map(min, enumerate(sorted(citations, reverse=True), 1))) if citations else 0
    return max(m) if citations else 0


def h_index_ii(citations: List[int]):
        return max(map(min, enumerate(sorted(citations, reverse=True), 1))) if citations else 0
