#Проверить работу всех предложенных к рассмотрению
# функций из встроенной библиотеки heapq
import heapq
a=list(map(int, input().split()))
heapq.heapify(a)
print(a)
el=int(input('Добавляемый элемент '))
heapq.heappush(a,el)
print(a)
heapq.heappop(a)
print(a)
heapq.heapreplace(a,589)
print(a)
heapq.heappushpop(a,47)
print(a)
print(heapq.nlargest(3,a,key=None))
print(heapq.nsmallest(3,a,key=None))
