import heapq as hq

def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        hq.heappush(scoville, hq.heappop(scoville) + hq.heappop(scoville)*2)
        cnt += 1
    if scoville[0] < K : return -1
    return cnt
