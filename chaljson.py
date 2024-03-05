import json


def is_json(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            json.loads(content)
            return True

    except (ValueError, FileNotFoundError) as e:
        print(f"read error of file :{e}")
        return False


filename = "/home/hypolit/project/pro2/test.txt"
if is_json(filename):
    print("yes it's a valid JSON")
else:
    print("\n it's a invalid JSON !")
