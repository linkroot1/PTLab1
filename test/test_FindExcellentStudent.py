# -*- coding: utf-8 -*-
from FindExcellentStudent import FindExcellentStudent
from src.Types import DataType
import pytest


class TestFindExcellentStudent:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, str]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 90),
                    ("программирование", 90),
                    ("литература", 97)
                ]
        }

        result: str = 'Петров Игорь Владимирович'

        return data, result

    def test_init_find_excellent_student(self, input_data: tuple[DataType,
                                                                 str]) -> None:
        find_student = FindExcellentStudent(input_data[0])
        assert input_data[0] == find_student.data

    def test_find(self, input_data: tuple[DataType, str]) -> None:
        result_name = FindExcellentStudent(input_data[0]).find()
        assert result_name == input_data[1]
