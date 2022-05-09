import os

def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''

    assert isinstance(fname,str)
    assert n > 0
    assert fname[-4:] == '.txt'

    f = open(fname,'r')
    line = list(f.readlines())

    file_size = os.path.getsize(fname)
    block_size = file_size / n

    lineSize = len(line)
    total = 0
    for i in range(lineSize):
        total += len(line[i])

    curline = 0
    curSize = 0

    for i in range(n):
        r_file = open(f'{fname}_{str(i).zfill(3)}.txt','wb')

        for j in range(len(line)):
            if curline == lineSize:
                break
            elif curSize + len(line[curline]) <= (i + 1) * block_size and curline <= lineSize:
                r_file.write(line[curline].encode())
                curSize += len(line[curline])
                curline += 1
            else:
                curline = curline
                curSize = curSize
                break
        r_file.close()

fname = 'lines.txt'
split_by_n(fname,3)
