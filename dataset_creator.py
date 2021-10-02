import csv
import os


def write(sum_list, minus_list, csv_path="data/dataset.csv"):
    cur_path = os.path.abspath(os.curdir)
    try:
        os.mkdir(cur_path + "/data")
        res = open(os.path.join(cur_path, csv_path), "x+")
    except FileExistsError:
        a = ""
    finally:
        var = None

    with open(os.path.join(cur_path, csv_path), 'w', newline='') as csv_file:
        fieldnames = ['i', 'j', 'operation', 'result']
        spam_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        spam_writer.writeheader()
        spam_writer.writerows(sum_list)
        spam_writer.writerows(minus_list)


def main(csv_path, length=100):
    sum_list = []
    minus_list = []

    for i in range(1, length):
        for j in range(1, length):
            sum_list.append({
                "i": i,
                "j": j,
                "operation": "0",
                "result": i + j
            })
            sum_list.append({
                "i": j,
                "j": i,
                "operation": "0",
                "result": j + i
            })
            minus_list.append({
                "i": i,
                "j": j,
                "operation": "1",
                "result": i - j
            })
            minus_list.append({
                "i": j,
                "j": i,
                "operation": "1",
                "result": j - i
            })
            # negative
            sum_list.append({
                "i": -i,
                "j": j,
                "operation": "0",
                "result": -i + j
            })
            sum_list.append({
                "i": -j,
                "j": i,
                "operation": "0",
                "result": -j + i
            })
            minus_list.append({
                "i": -i,
                "j": j,
                "operation": "1",
                "result": -i - j
            })
            minus_list.append({
                "i": -j,
                "j": i,
                "operation": "1",
                "result": -j - i
            })
    write(sum_list, minus_list, csv_path)
