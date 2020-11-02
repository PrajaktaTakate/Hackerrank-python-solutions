def solution(S):
    records = S.split("\n")
    print("Records", records)
    header = records[0]
    rows = list(map(lambda element: element.split(","), records[1:]))
    filtered_records = []
    print("Rows", rows)
    for row in rows:
        if 'NULL' not in row:
            filtered_records.append(row)
    print("filtered records:", filtered_records)
    result = [",".join(record) for record in filtered_records]
    result.insert(0, header)
    print("Result")
    print(result)
    return "\n".join(result)


# List comprehension
# Map and lambda
# Python generators

S1 = "id,name,salary\n1,kj,234\n2,NULL,7878\n3,praj,123"
S = "id,name,salary\n1,kj,234\n2,AUNULL,7878\n3,praj,123"
print(solution(S))

"""Records ['id,name,salary', '1,kj,234', '2,NULL,7878', '3,praj,123']
Rows [['1', 'kj', '234'], ['2', 'NULL', '7878'], ['3', 'praj', '123']]
filtered records: [['1', 'kj', '234'], ['3', 'praj', '123']]
Result['id,name,salary', '1,kj,234', '3,praj,123']
id,name,salary1,
kj,2343,praj,123"""

