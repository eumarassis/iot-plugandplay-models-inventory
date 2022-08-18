from dbrepository import DbRepository
from gitrepository import GitRepository
import json

def main():

    repo = DbRepository('pnpmodel.db')

    git_repo = GitRepository('C:\\Users\\eassis\\OneDrive - Microsoft\\Desktop\\TECHNICAL\\iot-plugandplay-models\\dtmi')


    for file_path in git_repo.get_all_model_file_path():
        data = None
        
        try:
            with open(file_path, encoding='utf-8') as json_file:
                data = json.load(json_file)
        
            model_content = git_repo.parse_model_json(data)

            repo.write_model (model_content)

            print("Completed writing model to db: " + file_path)
        except Exception as ex:
            print("Error writing model {} to db. Error {}".format( file_path,ex ) )



if __name__ == "__main__":
    main()