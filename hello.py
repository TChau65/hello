import pandas as pd


def create_dictionary():
    # create a dictionary
    data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

    # create a dataframe from the dictionary
    df = pd.DataFrame(data)

    print(df)

def create_two_dimensional_list():
    data = [['John', 25, 'New York'],
       ['Alice', 30, 'London'],
       ['Bob', 35, 'Paris']]

    # create a DataFrame from the list
    df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

    print(df)

def load_csv_file(filename):
    df = pd.read_csv(filename)
    print(df)


def main():
    # print("Hello World")
    # create_dictionary()
    # create_two_dimensional_list()
    filename =  'a.csv'
    load_csv_file(filename)

    pass


main()
