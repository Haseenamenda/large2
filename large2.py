def largest(arr,c):
	max=arr[0]
	for i in range(1,c):
                  if arr[i]>max:
                      	max=arr[i]
	return max
arr=[5, 4, 3, 2, 1, 7, 6, 10, 8, 9]
c=len(arr)
Ans=largest(arr,c)
print(Ans)
