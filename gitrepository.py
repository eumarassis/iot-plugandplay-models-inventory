
import os
import json

class GitRepository ():
    """Wrapper for SQLite"""

    def __init__(self, folder_path):

        self.folder_path = folder_path
       
                
    def get_all_model_file_path(self):
        file_paths = []

        for root, dirs, files in os.walk(self.folder_path):
            for name in files:
                file_path = os.path.join(root, name)

                if os.path.splitext(file_path)[1] == '.json':
                    file_paths += [file_path]

        return file_paths


    def parse_model_json (self, data):

        model_dict = {
            "id" : data['@id'],
            "type" : str(data['@type']),
            "context" : str( data['@context']),                
            "displayname" : data['displayName'],
            "description" : data['description'] if "description" in data else "",
            "contents" : list()
        }

        for capability in data['contents']:
            capability_dict = {
                "model_id" : data['@id'],
                "type" : str(capability['@type']),
                "name" : capability['name'],                
                "displayname" : capability['displayName'] if "displayName" in capability else "",
                "schema" : str(capability['schema']),
            }

            model_dict["contents"].append(capability_dict)

        return model_dict

