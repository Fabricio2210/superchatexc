import json
def read_chat(path, file):
    file_path = f"{path}/{file}"
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None