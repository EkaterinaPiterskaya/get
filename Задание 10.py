#Объединить две кучи в одну отсортированную
import heapq
a=list(map(int, input().split()))
b=list(map(int, input().split()))
heapq.heapify(a)
heapq.heapify(b)
twoheap=[]
for k in range (len(a)):
    twoheap.append(heapq.heappop(a))
for i in range (len(b)):
    twoheap.append(heapq.heappop(b))
heapq.heapify(twoheap)
print(twoheap)