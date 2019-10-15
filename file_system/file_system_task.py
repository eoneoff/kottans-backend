import os.path as p

try:
    with open('counter.txt', 'x') as f:
        f.write('1')
except FileExistsError:
    with open('counter.txt', 'r+') as f:
        data = f.read()
        try:
            int_data = int(data)
            f.seek(0)
            f.write(str(int_data + 1))
            f.truncate()
        except:
            pass