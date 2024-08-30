import sys

input = sys.stdin.readline

N = int(input())    #컴퓨터 개수
V = int(input())    #연결선 개수
graph = [[] for i in range(N+1)]    #그래프 초기화. 1번 컴을 1번 인덱스로 쓰기위해 N+1
visited = [0]*(N+1)     #방문한 그래프인지 표시. 

for i in range(V):
    com1, com2 = map(int, input().split())
    graph[com1] += [com2]   #com1에 com2 연결
    graph[com2] += [com1]   #com2에 com1 연결 -> 양방향

def dfs(v):  #방문할 컴퓨터 번호 v
    visited[v] = 1   #v를 방문했다고 표시
    for i in graph[v]:  #graph[v]는 v번 컴퓨터에 연결된 컴퓨터들의 리스트이다.
        if visited[i]==0:
            dfs(i)

dfs(1)  #1번 컴퓨터 방문을 시작으로, 연결된 컴퓨터들을 재귀 호출하며 방문
print(sum(visited)-1)  #1번 컴퓨터를 제외한 개수