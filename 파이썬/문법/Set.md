## 파이썬 set()에 대해서
### 집합 자료형의 특징
- 중복을 허용하지 않는다.
- 순서가 없다(Unordered)

집합 자료형은 다음과 같이 set 키워드로 만들 수 있다.
```python
A = set('apple')
B = set([1,2,3])
```

set에 문자열을 추가할 때, 위와 같이 넣으면 알파벳이 분리되어 집합에 들어간다.
{'a', 'p', 'l', 'e'}

```python
A = set()
A.add('apple')
```

set()으로 비어있는 set을 먼저 만들어주고, add()로 문자열을 추가하면 문자열 그대로 집합에 들어간다.
{'apple'}

### 교집합, 합집합, 차집합

다음과 같은 2개의 Set을 만들어보자.
'''python
>>> s1 = set([1,2,3,4,5,6])
>>> s2 = set([4,5,6,7,8,9])
'''

#### 교집합
'&'을 사용하면 교집합을 간단히 구할 수 있다.
<code>
>>> s1 & s2
{4, 5, 6}
</code>

또는 다음과 같이 intersection 함수를 사용해도 된다.
<code>
>>> s1.intersection(s2)
{4, 5, 6}
</code>

#### 합집합
'|'을 사용하면 합집합을 구할 수 있다.
<code>
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
</code>

또는 다음과 같이 union 함수를 사용해도 된다.
<code>
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
</code>

#### 차집합
'-'를 사용하면 차집합을 구할 수 있다.
<code>
>>> s1 - s2
{1, 2, 3}

>>> s2 - s1
{8, 9, 7}
</code>

또는 difference 함수를 사용해도 된다.
<code>
>>> s1.difference(s2)
{1, 2, 3}

>>> s2.difference(s1)
{8, 9, 7}
</code>

### 집합 자료형 관련 함수

#### 값 1개 추가하기 - add
<code>
>>> s1 = set([1, 2, 3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}
</code>

#### 값 여러 개 추가하기 - update
<code>
>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6])
>>> s1
{1, 2, 3, 4, 5, 6}
</code>

#### 특정 값 제거하기 - remove, discard
<code>
>>> s1 = set([1, 2, 3])
>>> s1.remove(2)
>>> s1
{1, 3}
</code>

discard()는 remove()와 똑같이 특정 요소를 제거할 때 사용하는데, remove()와는 달리 discard()는 요소가 Set에 존재하지 않는 경우에 KeyError를 발생시키지 않는다.
<code>
>>> s1 = set([1, 2, 3])
>>> s1.discard(2)
>>> s1
{1, 3}
</code>

#### in을 사용한 요소 확인
집합에 특정 요소가 있는지 in 연산자를 사용하여 확인할 수 있다.
값이 있다면 True, 없다면 False를 반환한다.

<code>
>>> fruits = {"apple", "banana", "cherry"}
>>> print("apple" in fruits)
>>> print("grape" in fruits)
True
False
</code>