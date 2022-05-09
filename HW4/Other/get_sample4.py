def threshold_values(seq,threshold=1):
    """

    :return:
    """

    assert isinstance(seq,list)
    assert isinstance(threshold,int)

    s = seq
    map = {}
    map2 = {}
    keyname = []

    for i in s:
        map[i] = []
    for i in s:
        string1 = i
        count0 = 0
        count1 = 0
        for j in string1:
            if j == '0':
                count0 = count0 + 1
            if j == '1':
                count1 = count1 + 1
        if count1 >= count0:
            map[string1].append(1)
        if count1 < count0:
            map[string1].append(0)


    for i in map.keys():
        if 1 in map[i]:
            map2[i] = len(map[i])  # map2里面是有1的计数

    print('map2',map2)

    for num in range(0,threshold):
        keyname.append(max(map2, key=map2.get))
        del map2[keyname[num]]   #keyname保留几个要留有1的key

    print(map2)
    print(keyname)

    map3 = map
    for i in map3.keys():
        if i in keyname:
            map3[i] = 1
        else:
            map3[i] = 0

    print(map3)


    return  map3

seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
threshold_values(seq,3)