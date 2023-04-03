def get_percents(filename):
    with open(filename, 'r') as report:
        lines = report.readlines()
    for i in lines:
        if '<td>Lines:</td>' in i:
            print(i.rfind('<td>'))
            print(i[i.rfind('<td>'):])
            print(i.find('</td>', i.rfind('<td>')))
            print(i[i.rfind('<td>') + 4:i.find('</td>', i.rfind('<td>')) - 1])
            return float(i[i.rfind('<td>') + 4:i.find('</td>', i.rfind('<td>')) - 1])