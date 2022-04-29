# problem-solving

## Python 자료형(List, Set, Dict) 메서드 시간 복잡도(Big-O)
- [List](#list)
- [Set](#set)
- [Dict](#dict)

### List
| Operation     | Example       | Big-O      | Notes                             |
|---------------|---------------|------------|-----------------------------------|
| Index         | l[i]          | O(1)       |                                   |
| Store         | l[i] = 0      | O(1)       |                                   |
| Length        | len(l)        | O(1)       |                                   |
| Append        | l.append(5)   | O(1)       | mostly: ICS-46 covers details     |
| Pop           | l.pop()       | O(1)       | same as l.pop(-1), popping at end |
| Clear         | l.clear()     | O(1)       | similar to l = []                 |
| Slice         | l[a:b]        | O(b-a)     | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N) |
| Extend        | l.extend(…)   | O(len(…))  | depends only on len of extension  |
| Construction  | list(…)       | O(len(…))  | depends on length of … iterable   |
| check ==, !=  | l1 == l2      | O(N)       |                                   |
| Insert        | l[a:b] = …    | O(N)       |                                   |
| Delete        | del l[i]      | O(N)       | depends on i; O(N) in worst case  |
| Containment   | x in/not in l | O(N)       | linearly searches list            |
| Copy          | l.copy()      | O(N)       | Same as l[:] which is O(N)        |
| Remove        | l.remove(…)   | O(N)       |                                   |
| Pop           | l.pop(i)      | O(N)       | O(N-i): l.pop(0):O(N) (see above) |
| Extreme value | min(l)/max(l) | O(N)       | linearly searches list for value  |
| Reverse       | l.reverse()   | O(N)       |                                   |
| Iteration     | for v in l:   | O(N)       | Worst: no return/break in loop    |
| Sort          | l.sort()      | O(N Log N) | key/reverse mostly doesn’t change |
| Multiply      | k*l           | O(k N)     | 5l is O(N): len(l)l is O(N**2)    |

### Set
| Operation      | Example       | Big-O            | Notes                                                      |
|----------------|---------------|------------------|------------------------------------------------------------|
| Length         | len(s)        | O(1)             |                                                            |
| Add            | s.add(5)      | O(1)             |                                                            |
| Containment    | x in/not in s | O(1)             | compare to list/tuple - O(N)                               |
| Remove         | s.remove(..)  | O(1)             | compare to list/tuple - O(N)                               |
| Discard        | s.discard(..) | O(1)             |                                                            |
| Pop            | s.pop()       | O(1)             | popped value “randomly” selected                           |
| Clear          | s.clear()     | O(1)             | similar to s = set()                                       |
| Construction   | set(…)        | O(len(…))        | depends on length of … iterable                            |
| check ==, !=   | s != t        | O(len(s))        | same as len(t); False in O(1) if the lengths are different |
| <=/<           | s <= t        | O(len(s))        | issubset                                                   |
| />=/>          | s >= t        | O(len(t))        | issuperset s <= t == t >= s                                |
| Union          | s             | t                | O(len(s)+len(t))                                           |
| Intersection   | s & t         | O(len(s)+len(t)) |                                                            |
| Difference     | s - t         | O(len(s)+len(t)) |                                                            |
| Symmetric Diff | s ^ t         | O(len(s)+len(t)) |                                                            |
| Iteration      | for v in s:   | O(N)             | Worst: no return/break in loop                             |
| Copy           | s.copy()      | O(N)             |                                                            |

### Dict
| Operation      | Example     | Big-O     | Notes                           |
|----------------|-------------|-----------|---------------------------------|
| Index          | d[k]        | O(1)      |                                 |
| Store          | d[k] = v    | O(1)      |                                 |
| Length         | len(d)      | O(1)      |                                 |
| Delete         | del d[k]    | O(1)      |                                 |
| get/setdefault | d.get(k)    | O(1)      |                                 |
| Pop            | d.pop(k)    | O(1)      |                                 |
| Pop item       | d.popitem() | O(1)      | popped item “randomly” selected |
| Clear          | d.clear()   | O(1)      | similar to s = {} or = dict()   |
| View           | d.keys()    | O(1)      | same for d.values()             |
| Construction   | dict(…)     | O(len(…)) | depends # (key,value) 2-tuples  |
| Iteration      | for k in d: | O(N)      | all forms: keys, values, items  |

***ref.***  
[Python - List, Set, Dict 자료형에 따른 시간 복잡도(Big-O)](https://2dowon.netlify.app/python/data-type-big-o/)

## Python3 vs PyPy3
> 파이썬은 인터프리터 언어로 코드를 한 줄씩 읽으며 기계어로 번역하여 실행한다. 
파이썬의 구현체인 **CPython**은 인터프리터이자 컴파일러로, 작성된 파이썬 코드를 바이트코드로 컴파일하고 실행한다.
>
> **PyPy**는 Cpython을 대체하는 구현체로 JIT 컴파일을 도입하여 CPython보다 빠르다고 알려져있다.  
> - JIT(just-in-time) 컴파일  
프로그램을 실행하기 전에 컴파일 하는 대신 프로그램을 실행하는 시점에서 필요한 부분들을 즉석으로 컴파일 하는 방식으로, 실행시 자주 쓰이는 코드를 캐싱하기 때문에 인터프리터의 느린 실행속도를 개선할 수 있음  
>
> 즉, PyPy3에서는 실행시 자주 쓰이는 코드를 캐싱하기 때문에 실행속도를 개선할 수 있다. (대신 그만큼 메모리를 더 사용한다.)
