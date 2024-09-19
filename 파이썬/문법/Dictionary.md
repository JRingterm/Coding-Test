## 파이썬 딕셔너리(dictionary)에 대해서

예시 문제 25206

딕셔너리는 단어 그대로 '사전'이라는 의미이다.
"people"이라는 단어에 "사람"이라는 뜻이 부합되듯이 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형이다.

<p>딕셔너리의 기본형</p>

```plaintext
{Key1: Value1, Key2: Value2, Key3: Value3, ...}
```

```python
dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
```

위와 같이, 등급에 따른 과목평점을 나타낼 때, 딕셔너리 형태로 만들어주면 A+라는 등급으로 4.5라는 평점을 가져올 수 있다.

```python
dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

print(dic["A+"])
#또는
dic.get("A+")
```

```plaintext
4.5
```

또한, Value를 이용해 Key를 찾을 수도 있다.
```python
[k for k, v in dic.items() if v == 4.5]
# 결과: ["A"]
```

하지만, Value로 Key를 자주 찾는다면, 매번 딕셔너리 전체를 순회하면서 가져오기 때문에 비효율 적이다.
다른 방법으로는 딕셔너리의 {key,value}를 뒤집어서 {value,key}로 저장해놓고 찾는 방법이 있다.

```python
dic = {"A+":4.5, "A0":4.0, "B+":3.5}
dic2 = dict(map(reversed, dic.items()))
print(dic2)
# 결과: {4.5: "A+", 4.0:"A0", 3.5:"B+"}

print(dic2[4.5])
# 결과: A+
```

하지만, 동일한 Value를 가진 딕셔너리를 reversed 할 경우, 가장 나중의 값으로 덮어쓰여지게 된다. (딕셔너리는 중복된 key 못가짐.)

## 값 추가하기
```python
dic = {}

dic["name"] = "호준" 
```

## 하나의 key에 여러가지 value를 넣기
예제문제 9375

딕셔너리 key에 value를 추가하고 싶다면, value를 리스트로 주고 append 하면 된다.

```python
dic = { 'name' : '7D 건조 망고',
        'ingredient' : ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
        'origin' : '필리핀',
        'type' : '당절임'}

# 값 추가하기
dic['ingredient'].append('꿀')
```

리스트로 선언하지 않은 value에 append하면 오류가 발생한다.
