from collections import defaultdict

def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

def dfs(node, visted, result):
    visted.append(node)
    result.append(node)
    for neighbor in adj_list.get(node, []):
        if neighbor not in visted:
            dfs(neighbor, visted, result)
visted = set()
result = []
dfs(start, visited, result)
return result
            