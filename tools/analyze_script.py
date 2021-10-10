import os

def analyze():
    with open('artifacts/analyze_artifact.csv', 'w+') as f_obj:
        f_obj.write('ya zapuskayus - 10.10')
        # изменение, которое я хочу увидеть в коммитах
    # filename, file_extension = os.path.splitext('/path/to/somefile.ext')

if __name__ == "__main__":
    analyze()
    print('hello world!')
