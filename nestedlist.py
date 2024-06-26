if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    lowest = min(record[1] for record in records)
    nolowest = [x for x in records if x[1] != lowest]
    lowest2 = min(record[1] for record in nolowest)
    lowests2nd = [x[0] for x in nolowest if x[1] == lowest2]
    lowests2nd.sort()
    for i in lowests2nd:
        print(i)
