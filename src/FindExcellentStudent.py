# -*- coding: utf-8 -*-
from Types import DataType


class FindExcellentStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.result_find_excellent_student: str = 'Студент не найден'

    def find(self) -> str:
        for key in self.data:
            name = key
            suitable_rating_count = 0
            for subject in self.data[key]:
                if subject[1] == 90:
                    suitable_rating_count += 1
            if suitable_rating_count >= 2:
                self.result_find_excellent_student = name
        return self.result_find_excellent_student
