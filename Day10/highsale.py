import csv
with open("sales.csv", "r") as ifl, open("high_sales.csv", "w", newline='') as ofl:
    reader=csv.DictReader(ifl)
    writer=csv.DictWriter(ofl,fieldnames=reader.fieldnames)

    writer.writeheader()

    for row in reader:
        if int(row["Amount"]) > 10000:
            writer.writerow(row)