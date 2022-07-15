import abc
import decimal
import typing

from uuid import UUID

from models import MaturaResults


class CodeFormula:
    # Set to initial year of concrete formula implementation. It will not affect what recruitment will be available for.
    year: typing.Optional[int] = None
    uuid: typing.Optional[UUID] = None  # MUST BE ALWAYS BE SET TO NEW UUID
    min_score: int = 0
    max_score: float = 100

    def __init__(
            self,
            *,
            field_of_study_id: typing.Optional[int] = None,
            formula_year: typing.Optional[int] = None,
            threshold: typing.Optional[float] = None,
            threshold_year: typing.Optional[int] = None,
            is_official_threshold: typing.Optional[bool] = None,
            special_requirements: typing.Optional[bool] = None,
            university_id: typing.Optional[int] = None,
            department_id: typing.Optional[int] = None,
    ):
        """
        You do not need to use this fields
        can be not available during calculation (as you can see - all fields are optional)
        """
        self.field_of_study_id = field_of_study_id
        self.formula_year = formula_year or self.year
        self.threshold = threshold
        self.threshold_year = threshold_year
        self.is_official_threshold = is_official_threshold
        self.special_requirements = special_requirements
        self.university_id = university_id
        self.department_id = department_id

    @staticmethod
    def round(n: typing.Union[int, float, decimal.Decimal]) -> int:
        """Proper rounding method"""
        return int(decimal.Decimal(n).to_integral(decimal.ROUND_HALF_UP))

    @abc.abstractmethod
    def calculate(self, matura_results: MaturaResults) -> float:
        """You should implement your algorithm here"""
        pass
