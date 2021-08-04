import os
import pickle
from config import connection
from trie import Trie


class Initialize:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__sentences_trie = Trie()  # the files lines trie data structure

    def parse(self):
        """
        Parses each file in the files directory - for each file,
        adds each line to the data structure (file content- using SQL and trie- using Trie)
        """
        file_num = 0
        for root, dirs, files in os.walk(self.__file_name):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf8') as f:
                    line_num = 0
                    for line in f:
                        # adds each line to the files content database and to the trie data structure
                        line = line.rstrip().lstrip()
                        if line[:-1] != "":
                            self.__sentences_trie.add_sentence(line, file_num, line_num)
                            self.insert_content(file_num, line, line_num)
                        line_num += 1
                self.insert_file_name(file_num, file)
                file_num += 1
                print('.', end="")
        print()

    def create_files_data_table(self):
        """
        Creates SQL data table for the files content
        """
        try:
            with connection.cursor() as cursor:
                query = "CREATE TABLE files_content (" \
                        "file_num int," \
                        "row_num int," \
                        "content VARCHAR(200)," \
                        "CONSTRAINT files_content PRIMARY KEY (file_num,row_num));"
                cursor.execute(query)
                connection.commit()
            with connection.cursor() as cursor:
                query = "CREATE TABLE files_names (" \
                        "file_num int," \
                        "file_name VARCHAR(40)," \
                        "CONSTRAINT files_names PRIMARY KEY (file_num,file_name));"
                cursor.execute(query)
                connection.commit()
        except:
            pass

    def insert_content(self, file_num, line, line_num):
        """
        Inserts line to the database
        """
        try:
            with connection.cursor() as cursor:
                query = "insert into files_content values (%s, %s, %s)"
                cursor.execute(query, (file_num, line_num, line))
                connection.commit()
        except:
            pass

    def insert_file_name(self, file_num, file_name):
        """
        Inserts the file serial number with its name to the database
        """
        try:
            with connection.cursor() as cursor:
                query2 = "insert into files_names values (%s, %s)"
                cursor.execute(query2, (file_num, file_name))
                connection.commit()
        except:
            pass

    def initialize_data(self):
        """
        Initializes the data structure, may run only once before beginning the program
        """
        self.create_files_data_table()
        self.parse()
        # writes the Trie object to a file
        with open('trie.pkl', 'wb') as output:
            pickle.dump(self.__sentences_trie, output, pickle.HIGHEST_PROTOCOL)
