import csv
import os
import soundfile

path="data"

def stats():
    with open('artifacts/stats_artifact.csv', 'w+') as f_obj:
        csv_writer = csv.writer(f_obj, delimiter=",")
        for root, dirs, files in os.walk(path):
            for file in files:
                data, sr = soundfile.read(f"data/{file}")
                filename, _ = os.path.splitext(file)
                csv_writer.writerow([filename, sr, data.shape[1]])
                print(filename, ',', sr, ',', data.shape[1])


if __name__ == "__main__":
    print('Start collecting statistic:\n')
    stats()
    print('\nCollection ended')