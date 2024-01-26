import pandas as pd

def open_excel_to_csv(file_name_excel:str, file_name_csv:str):
    """open excel file"""
    content = pd.read_excel(file_name_excel)
    content.to_csv(file_name_csv, index=False)
    print(f'{file_name_excel} converted in {file_name_csv}')


if __name__ == "__main__":
    file_name_excel = 'users.xlsx'
    file_name_csv = 'users.csv'
    open_excel_to_csv(file_name_excel, file_name_csv)


