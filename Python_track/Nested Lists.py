if __name__ == '__main__':
    records = []
    scores = []
    
    # stores records in to the records array
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        scores.append(score)
    
    # sorts both records and scores
    records.sort()
    scores = sorted(set(scores))
    # print(scores)
    
    # loops through the record and if the records score is equal to the second minimum it prints as result
    if len(scores) <= 1:
        print(records[0][0])
    else:
        for record in records:
            if record[1] == scores[1]:
                print(record[0])
         
