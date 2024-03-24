#Реализуйте алгоритм сортировки кучей.
# На вход подаётся неотсортированный список,
# на выходе должен получиться  отсортированный список
mas1=list(map(int,input().split(' ')))
def swap(arr, i1, i2):
    if arr[i1]<arr[i2]:
        arr[i1],arr[i2]=arr[i2],arr[i1]
def heap_sort(arr,length,i):
    while True:
        lower=2*i+2
        if lower<length:
            if arr[lower]<arr[lower-1]:
                swap(arr,i,lower-1)
                i=lower-1
            else:
                swap(arr,i,lower)
                i=lower
        else:
            if lower-1<length:
                swap(arr,i,lower-1)
            break
def make_a_mass(arr):
    for k in range(len(arr)//2,-1,-1):
        heap_sort(arr,len(arr),k)
    for k in range(len(arr)- 1,0,-1):
        arr[k],arr[0]=arr[0],arr[k]
        heap_sort(arr,k,0)
make_a_mass(mas1)
for i in range(len(mas1)):
    print(mas1[i],end =' ')