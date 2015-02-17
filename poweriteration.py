def powerIteration(matrix, columnVector):
    numIteration = 0
    while True:
        numIteration += 1
        tmpColumnVector= []
        for row in matrix:
            count = 0
            #print row
            for j in xrange(len(row)):
                count += (row[j] * columnVector[j])
            tmpColumnVector.append(count)
        ret = True
        for i in xrange(len(columnVector)):
            if tmpColumnVector[i] != columnVector[i]:
                ret = False
                break
        print tmpColumnVector
        if ret:
            print columnVector
            break
        columnVector = tmpColumnVector
        
def main():
    matrix = [[0,   0, 1], 
              [0.5, 0, 0],
              [0.5, 1, 0]
             ]
    columnVector = [1, 1, 1]
    powerIteration(matrix, columnVector)
    
if __name__ == '__main__':
    main()
