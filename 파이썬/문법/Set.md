## 파이썬 set()에 대해서

```python
A = set('apple')
```

set에 문자열을 추가할 때, 이렇게 넣으면 알파벳이 분리되어 집합에 들어간다.
{'a', 'p', 'l', 'e'}

```python
A = set()
A.add('apple')
```

set()으로 비어있는 set을 먼저 만들어주고, add()로 문자열을 추가하면 문자열 그대로 집합에 들어간다.
{'apple'}