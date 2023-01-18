import csv

with open('data/phone_book.csv', mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    line_count = 0
    for row in csv_reader:
        print(row['last_name'],' : ',int(row['phone_number']))
        line_count += 1
