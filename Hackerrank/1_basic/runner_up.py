"""Given the participants' score sheet for your University Sports Day,
 you are required to find the runner-up score.You are given  scores.
 Store them in a list and find the score of the runner-up."""

if __name__ == '__main__':
    n = 5
    score="2 3 6 6 5"
    arr = map(int, score.split())
    arr = list(arr)
    res = []
    [res.append(x) for x in arr if x not in res]
    print(res[1])


