import pandas as pd
import numpy as np
from datetime import datetime, timedelta 

def build_graph(input_csv, output_graph_csv):

    df = pd.read_csv(INPUT_PATH, usecols=["time","id","lat","long"])
    df.time = pd.to_datetime(df.time)

    proximity_threshold = 0.000015 # (approxi 1m); Important assumption, check for reasonable values and always report values chosen
    time_threshold = 10 # In minutes. Important assumption, check for reasonable values and always report values chosen
    final_list = []
    for index, row in df.iterrows():

        person = row['id']
        time = row['time']
        lat = row['lat']
        long = row['long']

        # Get rows whose geographically and temporally close to the "actual row" (by proximity_threshold and time_threshold) 
        geo_time_slice = df[(df['lat'].between(lat - proximity_threshold, lat + proximity_threshold,inclusive=True)) &
                            (df['long'].between(long - proximity_threshold, long + proximity_threshold,inclusive=True)) &
                            (df['time'].between(time + timedelta(minutes =- time_threshold), time + timedelta(minutes =+ time_threshold),inclusive=True)) &
                            (df['id'] != person)]
        
        final_list.append([person, time.strftime("%Y-%m-%d %H:%M:%S"), lat, long, geo_time_slice['id'].unique().tolist()])

    df_contact = pd.DataFrame(final_list, columns = ['id', 'time', 'lat','long','contact_list'])
    df_contact.to_csv(output_graph_csv,  index=False)
    return




if __name__ == "__main__":
    
    #change path of files 
    INPUT_PATH = "/Users/Etienne/Desktop/FaceAuVirus/confidential/sample_confidential_formatted.csv"
    OUTPUT_PATH = "/Users/Etienne/Desktop/FaceAuVirus/confidential/cg_sample_confidential_formatted.csv"

    build_graph(INPUT_PATH,OUTPUT_PATH)