import pandas as pd

messy_data_location = "MiniPythonProjects/Syntax_Speed_Builder/CSV_Cleaning_1/messy_generated.csv"

df = pd.read_csv(messy_data_location)

if df is not None:
    df.columns = df.columns.str.strip()
    df['name'] =  df['name'].str.strip().str.capitalize()

    df = df.drop_duplicates()
    df = df.dropna(subset=['name', 'age'])
    df = df.fillna("NA")
    df = df.replace({"not_available": "NA"})


    clean_file = "MiniPythonProjects/Syntax_Speed_Builder/CSV_Cleaning_1/cleaned_data.csv"

    df.to_csv(clean_file, sep='\t', encoding='utf-8', index=False)
else:
    print("Couldn't Find CSV File")

