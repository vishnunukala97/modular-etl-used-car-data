import pandas as pd
import xml.etree.ElementTree as ET
import glob

def extract_from_csv(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.lower()
    return df   
def extract_from_json(file):
    df = pd.read_json(file, lines=True)
    df.columns = df.columns.str.strip().str.lower()
    return df
 
def extract_from_xml(file):
    df = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file)
    root = tree.getroot()
    for record in root:
        model = record.find('car_model').text
        year = record.find('year_of_manufacture').text
        price = record.find('price').text
        fuel = record.find('fuel').text
        df = pd.concat([df, pd.DataFrame([{
            "car_model": model,
            "year_of_manufacture": year,
            "price": price,
            "fuel": fuel
        }])], ignore_index=True)
    return df

def extract_all_files(target_file="transformed_data.csv"):
    extracted_data = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])

    for csv_file in glob.glob("../*.csv"):
        if csv_file != target_file:
            extracted_data = pd.concat([extracted_data, extract_from_csv(csv_file)], ignore_index=True)

    for json_file in glob.glob("../*.json"):
        extracted_data = pd.concat([extracted_data, extract_from_json(json_file)], ignore_index=True)

    for xml_file in glob.glob("../*.xml"):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xml_file)], ignore_index=True)

    return extracted_data


