def largest( arr, n):
    # arr.sort()
    # return arr[n-1]
    maxi=0
    for i in range(n):
        maxi = max(maxi,arr[i])
    return maxi
