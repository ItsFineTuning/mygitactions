import os

path="data"

def analyze():
    with open('artifacts/stats_artifact.csv', 'w+') as f_obj:
        f_obj.write('ya zapuskayus - statistics 10.10 15:14')
        for root, dirs, files in os.walk(path):
            for file in files:
                print(file)

    # filename, file_extension = os.path.splitext('/path/to/somefile.ext')

if __name__ == "__main__":
    analyze()
    # print('Hello world!')