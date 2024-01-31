import pandas as pd

def create_excel_content(file_name_excel:str):
    """write columns and rows with data"""
    data = {'name': ['gabi', 'alin', 'joita'],
            'password': [1234, 5678, 9101],
            'username': ['gabi_123', 'alin_456', 'joita_789'],
            'e-mail': ['gabi@gmail', 'alin@yahoo.com', 'joita@email.com']}
    df = pd.DataFrame(data)
    with pd.ExcelWriter(file_name_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

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
    print(create_excel_content(file_name_excel))
    print(open_excel_to_csv(file_name_excel, file_name_csv))
    print(open_file_csv(file_name_csv))
    print(open_file_txt(file_name_txt))
