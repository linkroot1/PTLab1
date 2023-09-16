# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}


    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            students_dict = json.load(file)
            key = students_dict.keys()
            for key in students_dict:
                self.key = key
                self.students[self.key] = []
                subjects = students_dict[key]
                for subjects in students_dict[key]:
                    subject_name = subjects
                    self.students[self.key].append(
                    (subject_name, students_dict[key][subject_name]))
        return self.students
