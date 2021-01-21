import pandas as pd


def main():
    train_csv_file = r"C:\Users\razik\cs50\ai_basics\Lesson1\Titanic\train.csv"
    train_data = pd.read_csv(train_csv_file)
    print(train_data.head())

if __name__ == "__main__":
    main()