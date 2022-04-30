# 처음에 이렇게 풀었다가 (-> 가독성 전멸 수준)
def solution(id_list, report, k):
    answer = []
    reported = {user:0 for user in id_list}
    report_list = {user:set() for user in id_list}
    black_list = set()
    
    for r in report:
        a, b = r.split()[0], r.split()[1]
        if b not in report_list[a]:
            report_list[a].add(b)
            reported[b] += 1
            if reported[b] >= k: black_list.add(b)
              
    for user, repo in report_list.items():
        answer.append(len(repo & black_list))
        
    return answer
  
  
  
# 입력으로 들어오는 report를 set()으로 바꿨더니 코드가 정말 간단해졌다.... 중복을 제거하고 시작하면 된다는 걸 뒤늦게 깨달았다
def solution(id_list, report, k):
    report_list = {user:set() for user in id_list}
    for r in set(report): report_list[r.split()[0]].add(r.split()[1])
      
    reported = {user:0 for user in id_list}    
    for r in set(report): reported[r.split()[1]] += 1
    
    black_list = set([user for user, cnt in reported.items() if cnt >= k])
    
    answer = [len(repo & black_list) for repo in report_list.values()]
    return answer
