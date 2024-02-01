import pandas as pd

def open_excel_to_csv(file_name_excel: str, file_name_csv: str):
    """open excel file"""
    content = pd.read_excel(file_name_excel)
    content.to_csv(file_name_csv, index=False)
    return content


def open_file_csv(file_name_csv: str):
    """open csv file"""
    with open(file_name_csv, 'r') as rd:
        content = rd.read()
    return content


def open_file_txt(file_name_txt: str):
    """open the previews files in txt"""
    with open(file_name_txt, 'w') as fr:
        fr.write(open_file_csv(file_name_csv))
    return open_file_csv(file_name_txt)


if __name__ == "__main__":
    file_name_excel = 'users.xlsx'
    file_name_csv = 'users.csv'
    file_name_txt = 'users.txt'
    print(open_excel_to_csv(file_name_excel, file_name_csv))
    print(open_file_csv(file_name_csv))
    print(open_file_txt(file_name_txt))
