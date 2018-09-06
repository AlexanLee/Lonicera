# _*_coding:utf-8_*_

def main():
    file = open('/data/challenge/round1_ijcai_18_train_20180301.txt')
    sum = 0
    total = 0
    for line in file:
        l = line.split(" ")
        # print(len(l))
        if total == 0:
            total += 1
            continue
        if int(l[26]) == 1:
            sum += 1
        total += 1
    print("total:%s,sum:%s", total, sum)


if __name__ == '__main__':
    main()
