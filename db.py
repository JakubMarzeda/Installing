# WZORZEC PROJEKTOWY SINGLETONA GWARANTUJACY NAM ZE TYLKO
# JEDNA INSTANCJA BAZY BEDZIE
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


import pyodbc as pyodbc


@singleton
class DataBase:

    # KONSTRUKTOR
    def __init__(self):
        self.connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                                  "Server=localhost;"
                                  "Database=Installing;"
                                  "Trusted_Connection=yes;")
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def select_english_word(self, id):
        self.cursor.execute(f"SELECT EnglishWord FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]
    def select_polish_word(self, id):
        self.cursor.execute(f"SELECT PolishWord FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]
    def select_sentence_with_gap(self, id):
        self.cursor.execute(f"SELECT SentenceWithGap FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]
    def select_sentence_without_gap(self, id):
        self.cursor.execute(f"SELECT SentenceWithoutGap FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]