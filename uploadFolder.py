import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dir, files in os.walk(file_from):
            for f in files:
                local_path = root + '/' + f
                print(local_path)
                dropbox_path = file_to + '/' + local_path
                print(dropbox_path)

                with open(local_path, 'rb') as h:
                    dbx.files_upload(h.read(), dropbox_path)## , mode = WriteMode('overwrite')

def main():
    access_token = 'Sc2wo30nYcsAAAAAAAAAATn3gYqNozHLJXYDiO64o-We6b-2TFfXC2oWd07bkBeP'
    transferData = TransferData(access_token)

    file_from = 'testFolder'
    file_to = '/Python/test_dropbox/testFolder'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Files Uploaded")

main()