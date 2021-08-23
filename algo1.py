def sort(arr):
    for i in range (1,len(arr)):
      key=arr[i]
      j=i-1

      while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j=j-1

      arr[j+1]=key

arr=[44,12,88,18,9,105,44]
sort(arr)
for i in range (len(arr)):
    print(arr[i])
