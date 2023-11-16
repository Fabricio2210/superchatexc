import os
from  getDataSuperchats import read_chat
from getDataParsed import get_data_parsed
from excel import excel
import timeit

def wrapper(subject,folder):
     directory = f'./{subject}/{folder}'
     startTime = timeit.default_timer()
     for file in os.listdir(directory):
        if file.endswith(".json"):
            try:
                data_info = read_chat(directory, file)
                if data_info:
                    info_to_excel = get_data_parsed(data_info)
                    excel(info_to_excel, file, subject)
            except Exception as error:
                print(f"Error processing file {file}: {error}")
            endTime = timeit.default_timer()
            elapsedTime = endTime - startTime
            print(f"Time taken: {elapsedTime} seconds")