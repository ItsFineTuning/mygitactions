import os

def analyze():
    with open('statistics.csv', 'w') as f_obj:
        f_obj.write('ya zapuskayus - statistics')
    # filename, file_extension = os.path.splitext('/path/to/somefile.ext')

if __name__ == "__main__":
    analyze()