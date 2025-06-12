print("Hello world!")

def faboncai(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    result = [1, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result