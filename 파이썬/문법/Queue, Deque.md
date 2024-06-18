## Queue와 Deque의 차이점!
파이썬에서 queue와 deque의 차이를 알아보았다.

### queue
queue는 멀티 스레드 환경에서 스레드 간의 안전한 소통을 위해 만들어진 <b>라이브러리</b>이다.

queue에서 활용 가능한 메소드들을 보면 이를 확인할 수 있다.

```python
from queue import Queue

queue = Queue()
dir(queue)
```

위 코드를 통해 살펴보면 단순한 put, get외에도 put_nowait, get_nowait, task_done, join 등의 멀티 스레드 환경에서 사용되는 메소드들이 존재하는 것을 확인할 수 있다.

### deque
deque는 queue와는 다리 파이썬의 <b>자료구조</b>의 일종이다.
deque은 collections 라이브러리에서 import 되는데, 이 collections 라이브러리는 container datatype이다.

```python
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
deq = deque(range(1,N+1))
```

공식 문서에서도 deque은 list와 비슷하게 동작하지만, 그 연산의 복잡도에 있어 deque이 더 빠르게 동작하도록 설계되어 있다고 한다. (양 방향 입출력 모두 O(1))

따라서 파이썬에서는 deque가 queue보다 더 빠르다!

## 참고 문제 2164