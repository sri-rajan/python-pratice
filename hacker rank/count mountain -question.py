def countingValleys(steps, path):
    value=0
    count=0
    for i in range(steps):
        ans=path[i]
        if ans=="U":
            value+=1
        else:
            value+=-1
        if value==0 and ans=="U":
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
