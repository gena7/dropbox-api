# coding: UTF-8

import dropbox
import csv
import os
from os.path import join, dirname
from dotenv import load_dotenv


class DropboxApi():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    DB_ACCESS_TOKEN = os.environ.get('DB_ACCESS_TOKEN')
    DB_ROOT_DIR = ''

    def __init__(self):
        self.dbx = dropbox.Dropbox(self.DB_ACCESS_TOKEN)

    def viewFiles(self):
        res = self.dbx.files_list_folder(self.DB_ROOT_DIR, recursive=True)

        self.__get_files_recursive(res)

    def __get_files_recursive(self, res):
        with open('./dropbox.csv', 'w') as f:
            writer = csv.writer(f)
            for entry in res.entries:
                ins = type(entry)
                if ins is not dropbox.files.FileMetadata:
                    continue

                link = self.__get_shared_link(entry.path_lower)
                if bool(link):
                    row = list()
                    row.append(entry.path_display)
                    row.append(link)
                    print(row)
                    writer.writerow(row)

            if res.has_more:
                res2 = self.dbx.files_list_folder_continue(res.cursor)
                self.__get_files_recursive(res2)

    def __get_shared_link(self, path):
        links = (
            self.dbx.sharing_list_shared_links(
                path=path, direct_only=True
            ).links
        )

        if links is not None:
            for link in links:
                return link.url


if __name__ == '__main__':
    DropboxApi().viewFiles()
