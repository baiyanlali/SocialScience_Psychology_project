import csv
import numpy

from epoch import epoch


def levenshtein(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]


def sovleCSV():
    f = csv.reader(open('testcollect.CSV', 'r'))
    rows = [row for row in f]
    epoches = []
    for e in rows:
        gender = e[0]
        if gender== '':
            break
        time=e[1]
        speciality=e[2]
        age=e[3]
        ep=epoch(gender,time,speciality,age)
        epoches.append(ep)
        for i in range(4,16,2):
            ep.corret.append(levenshtein(e[i],e[i+1]))

    with open("result.csv", 'a',newline='') as f:
        write = csv.writer(f)
        # row = ['性别', '时段', '专业', '年龄', '题1','题2','题3','题4','题5','题6']
        # write.writerow(row)
        for e in epoches:
            row=[e.gender,e.time,e.secialty,e.age]
            for correct in e.corret:
                row.append(correct)
            write.writerow(row)
        print("写入完毕！")





if __name__ == "__main__":
    sovleCSV()
