import dataclasses
import typing


@dataclasses.dataclass
class MaturaResults:
    biology: int = 0
    biology_advanced: int = 0
    chemistry: int = 0
    chemistry_advanced: int = 0
    civics: int = 0
    civics_advanced: int = 0
    dance: int = 0
    dance_advanced: int = 0
    geography: int = 0
    geography_advanced: int = 0
    history: int = 0
    history_advanced: int = 0
    history_of_art: int = 0
    history_of_art_advanced: int = 0
    history_of_music: int = 0
    history_of_music_advanced: int = 0
    informatics: int = 0
    informatics_advanced: int = 0
    language_be: int = 0
    language_be_advanced: int = 0
    language_be_oral: int = 0
    language_de: int = 0
    language_de_advanced: int = 0
    language_de_bilang: int = 0
    language_de_bilang_oral: int = 0
    language_de_oral: int = 0
    language_en: int = 0
    language_en_advanced: int = 0
    language_en_bilang: int = 0
    language_en_bilang_oral: int = 0
    language_en_oral: int = 0
    language_es: int = 0
    language_es_advanced: int = 0
    language_es_bilang: int = 0
    language_es_bilang_oral: int = 0
    language_es_oral: int = 0
    language_fr: int = 0
    language_fr_advanced: int = 0
    language_fr_bilang: int = 0
    language_fr_bilang_oral: int = 0
    language_fr_oral: int = 0
    language_it: int = 0
    language_it_advanced: int = 0
    language_it_bilang: int = 0
    language_it_bilang_oral: int = 0
    language_it_oral: int = 0
    language_kaszubski_advanced: int = 0
    language_kaszubski_oral: int = 0
    language_la_ancient_culture_advanced: int = 0
    language_lemkowski_advanced: int = 0
    language_lemkowski_oral: int = 0
    language_lt: int = 0
    language_lt_advanced: int = 0
    language_lt_oral: int = 0
    language_pl: int = 0
    language_pl_advanced: int = 0
    language_pl_oral: int = 0
    language_ru: int = 0
    language_ru_advanced: int = 0
    language_ru_bilang: int = 0
    language_ru_bilang_oral: int = 0
    language_ru_oral: int = 0
    language_uk: int = 0
    language_uk_advanced: int = 0
    language_uk_oral: int = 0
    math: int = 0
    math_advanced: int = 0
    philosophy: int = 0
    philosophy_advanced: int = 0
    physics_advanced: int = 0
    physics_astronomy: int = 0
    physics_astronomy_advanced: int = 0
    special_exam: int = 0
    special_fitness: int = 0
    special_interview: int = 0
    special_portfolio: int = 0
    language_de_minor_advanced: int = 0
    language_de_minor_oral: int = 0
    professional_exam: int = 0

    @classmethod
    def min_results(cls) -> 'MaturaResults':
        return cls()

    @classmethod
    def max_results(cls) -> 'MaturaResults':
        return cls.all_same_results(100)

    @classmethod
    def all_same_results(cls, score: int) -> 'MaturaResults':
        return cls(
            biology=score,
            biology_advanced=score,
            chemistry=score,
            chemistry_advanced=score,
            civics=score,
            civics_advanced=score,
            dance=score,
            dance_advanced=score,
            geography=score,
            geography_advanced=score,
            history=score,
            history_advanced=score,
            history_of_art=score,
            history_of_art_advanced=score,
            history_of_music=score,
            history_of_music_advanced=score,
            informatics=score,
            informatics_advanced=score,
            language_be=score,
            language_be_advanced=score,
            language_be_oral=score,
            language_de=score,
            language_de_advanced=score,
            language_de_bilang=score,
            language_de_bilang_oral=score,
            language_de_oral=score,
            language_en=score,
            language_en_advanced=score,
            language_en_bilang=score,
            language_en_bilang_oral=score,
            language_en_oral=score,
            language_es=score,
            language_es_advanced=score,
            language_es_bilang=score,
            language_es_bilang_oral=score,
            language_es_oral=score,
            language_fr=score,
            language_fr_advanced=score,
            language_fr_bilang=score,
            language_fr_bilang_oral=score,
            language_fr_oral=score,
            language_it=score,
            language_it_advanced=score,
            language_it_bilang=score,
            language_it_bilang_oral=score,
            language_it_oral=score,
            language_kaszubski_advanced=score,
            language_kaszubski_oral=score,
            language_la_ancient_culture_advanced=score,
            language_lemkowski_advanced=score,
            language_lemkowski_oral=score,
            language_lt=score,
            language_lt_advanced=score,
            language_lt_oral=score,
            language_pl=score,
            language_pl_advanced=score,
            language_pl_oral=score,
            language_ru=score,
            language_ru_advanced=score,
            language_ru_bilang=score,
            language_ru_bilang_oral=score,
            language_ru_oral=score,
            language_uk=score,
            language_uk_advanced=score,
            language_uk_oral=score,
            math=score,
            math_advanced=score,
            philosophy=score,
            philosophy_advanced=score,
            physics_advanced=score,
            physics_astronomy=score,
            physics_astronomy_advanced=score,
            special_exam=score,
            special_fitness=score,
            special_interview=score,
            special_portfolio=score,
            language_de_minor_advanced=score,
            language_de_minor_oral=score,
            professional_exam=score,
        )

    @property
    def any_foreign(self) -> int:
        return max(self.all_foreign)

    @property
    def all_foreign(self) -> typing.List[int]:
        return [
            self.language_de,
            self.language_en,
            self.language_es,
            self.language_fr,
            self.language_it,
            self.language_ru,
        ]

    @property
    def any_foreign_advanced(self) -> int:
        return max(self.all_foreign_advanced)

    @property
    def all_foreign_advanced(self) -> typing.List[int]:
        return [
            self.language_de_advanced,
            self.language_en_advanced,
            self.language_es_advanced,
            self.language_fr_advanced,
            self.language_it_advanced,
            self.language_ru_advanced,
        ]

    @property
    def all_minority_foreign(self) -> typing.List[int]:
        return [
            self.language_be,
            self.language_lt,
            self.language_uk,
        ]

    @property
    def any_minority_foreign(self) -> int:
        return max(self.all_minority_foreign)

    @property
    def all_minority_foreign_advanced(self) -> typing.List[int]:
        return [
            self.language_be_advanced,
            self.language_lt_advanced,
            self.language_uk_advanced,
            self.language_de_minor_advanced,
        ]

    @property
    def any_minority_foreign_advanced(self) -> int:
        return max(self.all_minority_foreign_advanced)

    @property
    def all_minority_foreign_oral(self) -> typing.List[int]:
        return [
            self.language_be_oral,
            self.language_lt_oral,
            self.language_uk_oral,
            self.language_de_minor_oral,
        ]

    @property
    def all_ethnic_language_advanced(self) -> typing.List[int]:
        return [
            self.language_lemkowski_advanced,
            self.language_kaszubski_advanced,
        ]

    @property
    def any_ethnic_language_advanced(self) -> int:
        return max(self.all_ethnic_language_advanced)

    @property
    def all_foreign_bilang(self) -> typing.List[int]:
        return [
            self.language_de_bilang,
            self.language_en_bilang,
            self.language_es_bilang,
            self.language_fr_bilang,
            self.language_it_bilang,
            self.language_ru_bilang,
        ]

    @property
    def any_foreign_bilang(self) -> int:
        return max(self.all_foreign_bilang)

    @property
    def any_foreign_oral(self) -> int:
        return max([
            self.language_de_oral,
            self.language_en_oral,
            self.language_es_oral,
            self.language_fr_oral,
            self.language_it_oral,
            self.language_ru_oral,
        ])

    @property
    def any_foreign_bilang_oral(self) -> int:
        return max([
            self.language_de_bilang_oral,
            self.language_en_bilang_oral,
            self.language_es_bilang_oral,
            self.language_fr_bilang_oral,
            self.language_it_bilang_oral,
            self.language_ru_bilang_oral,
        ])

    @property
    def any_physics_advanced(self) -> int:
        return max([self.physics_advanced, self.physics_astronomy_advanced])

    @property
    def biology_pair(self) -> typing.Tuple[int, int]:
        return (self.biology, self.biology_advanced)

    @property
    def chemistry_pair(self) -> typing.Tuple[int, int]:
        return (self.chemistry, self.chemistry_advanced)

    @property
    def civics_pair(self) -> typing.Tuple[int, int]:
        return (self.civics, self.civics_advanced)

    @property
    def dance_pair(self) -> typing.Tuple[int, int]:
        return (self.dance, self.dance_advanced)

    @property
    def geography_pair(self) -> typing.Tuple[int, int]:
        return (self.geography, self.geography_advanced)

    @property
    def history_pair(self) -> typing.Tuple[int, int]:
        return (self.history, self.history_advanced)

    @property
    def history_of_art_pair(self) -> typing.Tuple[int, int]:
        return (self.history_of_art, self.history_of_art_advanced)

    @property
    def history_of_music_pair(self) -> typing.Tuple[int, int]:
        return (self.history_of_music, self.history_of_music_advanced)

    @property
    def informatics_pair(self) -> typing.Tuple[int, int]:
        return (self.informatics, self.informatics_advanced)

    @property
    def language_be_pair(self) -> typing.Tuple[int, int]:
        return (self.language_be, self.language_be_advanced)

    @property
    def language_de_pair(self) -> typing.Tuple[int, int]:
        return (self.language_de, self.language_de_advanced)

    @property
    def language_en_pair(self) -> typing.Tuple[int, int]:
        return (self.language_en, self.language_en_advanced)

    @property
    def language_es_pair(self) -> typing.Tuple[int, int]:
        return (self.language_es, self.language_es_advanced)

    @property
    def language_fr_pair(self) -> typing.Tuple[int, int]:
        return (self.language_fr, self.language_fr_advanced)

    @property
    def language_it_pair(self) -> typing.Tuple[int, int]:
        return (self.language_it, self.language_it_advanced)

    @property
    def language_lt_pair(self) -> typing.Tuple[int, int]:
        return (self.language_lt, self.language_lt_advanced)

    @property
    def language_pl_pair(self) -> typing.Tuple[int, int]:
        return (self.language_pl, self.language_pl_advanced)

    @property
    def language_ru_pair(self) -> typing.Tuple[int, int]:
        return (self.language_ru, self.language_ru_advanced)

    @property
    def language_uk_pair(self) -> typing.Tuple[int, int]:
        return (self.language_uk, self.language_uk_advanced)

    @property
    def math_pair(self) -> typing.Tuple[int, int]:
        return (self.math, self.math_advanced)

    @property
    def philosophy_pair(self) -> typing.Tuple[int, int]:
        return (self.philosophy, self.philosophy_advanced)

    @property
    def physics_pair(self) -> typing.Tuple[int, int]:
        return (self.physics_astronomy, self.any_physics_advanced)

    @property
    def foreign_pairs(self) -> typing.List[typing.Tuple[int, int]]:
        return [
            self.language_de_pair,
            self.language_en_pair,
            self.language_es_pair,
            self.language_fr_pair,
            self.language_it_pair,
            self.language_ru_pair,
        ]


class SubjectNames(enum.Enum):
    BIOLOGY = 'biology'
    BIOLOGY_ADVANCED = 'biology_advanced'
    CHEMISTRY = 'chemistry'
    CHEMISTRY_ADVANCED = 'chemistry_advanced'
    CIVICS = 'civics'
    CIVICS_ADVANCED = 'civics_advanced'
    DANCE = 'dance'
    DANCE_ADVANCED = 'dance_advanced'
    GEOGRAPHY = 'geography'
    GEOGRAPHY_ADVANCED = 'geography_advanced'
    HISTORY = 'history'
    HISTORY_ADVANCED = 'history_advanced'
    HISTORY_OF_ART = 'history_of_art'
    HISTORY_OF_ART_ADVANCED = 'history_of_art_advanced'
    HISTORY_OF_MUSIC = 'history_of_music'
    HISTORY_OF_MUSIC_ADVANCED = 'history_of_music_advanced'
    INFORMATICS = 'informatics'
    INFORMATICS_ADVANCED = 'informatics_advanced'
    LANGUAGE_BE = 'language_be'
    LANGUAGE_BE_ADVANCED = 'language_be_advanced'
    LANGUAGE_BE_ORAL = 'language_be_oral'
    LANGUAGE_DE = 'language_de'
    LANGUAGE_DE_ADVANCED = 'language_de_advanced'
    LANGUAGE_DE_BILANG = 'language_de_bilang'
    LANGUAGE_DE_BILANG_ORAL = 'language_de_bilang_oral'
    LANGUAGE_DE_ORAL = 'language_de_oral'
    LANGUAGE_EN = 'language_en'
    LANGUAGE_EN_ADVANCED = 'language_en_advanced'
    LANGUAGE_EN_BILANG = 'language_en_bilang'
    LANGUAGE_EN_BILANG_ORAL = 'language_en_bilang_oral'
    LANGUAGE_EN_ORAL = 'language_en_oral'
    LANGUAGE_ES = 'language_es'
    LANGUAGE_ES_ADVANCED = 'language_es_advanced'
    LANGUAGE_ES_BILANG = 'language_es_bilang'
    LANGUAGE_ES_BILANG_ORAL = 'language_es_bilang_oral'
    LANGUAGE_ES_ORAL = 'language_es_oral'
    LANGUAGE_FR = 'language_fr'
    LANGUAGE_FR_ADVANCED = 'language_fr_advanced'
    LANGUAGE_FR_BILANG = 'language_fr_bilang'
    LANGUAGE_FR_BILANG_ORAL = 'language_fr_bilang_oral'
    LANGUAGE_FR_ORAL = 'language_fr_oral'
    LANGUAGE_IT = 'language_it'
    LANGUAGE_IT_ADVANCED = 'language_it_advanced'
    LANGUAGE_IT_BILANG = 'language_it_bilang'
    LANGUAGE_IT_BILANG_ORAL = 'language_it_bilang_oral'
    LANGUAGE_IT_ORAL = 'language_it_oral'
    LANGUAGE_KASZUBSKI_ADVANCED = 'language_kaszubski_advanced'
    LANGUAGE_KASZUBSKI_ORAL = 'language_kaszubski_oral'
    LANGUAGE_LA_ANCIENT_CULTURE_ADVANCED = 'language_la_ancient_culture_advanced'
    LANGUAGE_LEMKOWSKI_ADVANCED = 'language_lemkowski_advanced'
    LANGUAGE_LEMKOWSKI_ORAL = 'language_lemkowski_oral'
    LANGUAGE_LT = 'language_lt'
    LANGUAGE_LT_ADVANCED = 'language_lt_advanced'
    LANGUAGE_LT_ORAL = 'language_lt_oral'
    LANGUAGE_PL = 'language_pl'
    LANGUAGE_PL_ADVANCED = 'language_pl_advanced'
    LANGUAGE_PL_ORAL = 'language_pl_oral'
    LANGUAGE_RU = 'language_ru'
    LANGUAGE_RU_ADVANCED = 'language_ru_advanced'
    LANGUAGE_RU_BILANG = 'language_ru_bilang'
    LANGUAGE_RU_BILANG_ORAL = 'language_ru_bilang_oral'
    LANGUAGE_RU_ORAL = 'language_ru_oral'
    LANGUAGE_UK = 'language_uk'
    LANGUAGE_UK_ADVANCED = 'language_uk_advanced'
    LANGUAGE_UK_ORAL = 'language_uk_oral'
    MATH = 'math'
    MATH_ADVANCED = 'math_advanced'
    PHILOSOPHY = 'philosophy'
    PHILOSOPHY_ADVANCED = 'philosophy_advanced'
    PHYSICS_ADVANCED = 'physics_advanced'
    PHYSICS_ASTRONOMY = 'physics_astronomy'
    PHYSICS_ASTRONOMY_ADVANCED = 'physics_astronomy_advanced'
    SPECIAL_EXAM = 'special_exam'
    SPECIAL_FITNESS = 'special_fitness'
    SPECIAL_INTERVIEW = 'special_interview'
    SPECIAL_PORTFOLIO = 'special_portfolio'
    LANGUAGE_DE_MINOR_ADVANCED = 'language_de_minor_advanced'
    LANGUAGE_DE_MINOR_ORAL = 'language_de_minor_oral'
    PROFESSIONAL_EXAM = 'professional_exam'

    @classmethod
    @property
    def all_exams_advanced(cls) -> typing.List['SubjectNames']:
        return [
            cls.BIOLOGY_ADVANCED,
            cls.CHEMISTRY_ADVANCED,
            cls.CIVICS_ADVANCED,
            cls.DANCE_ADVANCED,
            cls.GEOGRAPHY_ADVANCED,
            cls.HISTORY_ADVANCED,
            cls.HISTORY_OF_ART_ADVANCED,
            cls.HISTORY_OF_MUSIC_ADVANCED,
            cls.INFORMATICS_ADVANCED,
            cls.LANGUAGE_BE_ADVANCED,
            cls.LANGUAGE_DE_ADVANCED,
            cls.LANGUAGE_EN_ADVANCED,
            cls.LANGUAGE_ES_ADVANCED,
            cls.LANGUAGE_FR_ADVANCED,
            cls.LANGUAGE_IT_ADVANCED,
            cls.LANGUAGE_KASZUBSKI_ADVANCED,
            cls.LANGUAGE_LA_ANCIENT_CULTURE_ADVANCED,
            cls.LANGUAGE_LEMKOWSKI_ADVANCED,
            cls.LANGUAGE_LT_ADVANCED,
            cls.LANGUAGE_PL_ADVANCED,
            cls.LANGUAGE_RU_ADVANCED,
            cls.LANGUAGE_UK_ADVANCED,
            cls.MATH_ADVANCED,
            cls.PHILOSOPHY_ADVANCED,
            cls.PHYSICS_ADVANCED,
            cls.PHYSICS_ASTRONOMY_ADVANCED,
            cls.LANGUAGE_DE_MINOR_ADVANCED,
        ]

    @classmethod
    @property
    def all_exams_base(cls) -> typing.List['SubjectNames']:
        return [
            cls.BIOLOGY,
            cls.CHEMISTRY,
            cls.CIVICS,
            cls.DANCE,
            cls.GEOGRAPHY,
            cls.HISTORY,
            cls.HISTORY_OF_ART,
            cls.HISTORY_OF_MUSIC,
            cls.INFORMATICS,
            cls.LANGUAGE_BE,
            cls.LANGUAGE_DE,
            cls.LANGUAGE_EN,
            cls.LANGUAGE_ES,
            cls.LANGUAGE_FR,
            cls.LANGUAGE_IT,
            cls.LANGUAGE_LT,
            cls.LANGUAGE_PL,
            cls.LANGUAGE_RU,
            cls.LANGUAGE_UK,
            cls.MATH,
            cls.PHILOSOPHY,
            cls.PHYSICS_ASTRONOMY,
        ]

    @classmethod
    @property
    def all_foreign_base(cls) -> typing.List['SubjectNames']:
        return [
            cls.LANGUAGE_DE,
            cls.LANGUAGE_EN,
            cls.LANGUAGE_ES,
            cls.LANGUAGE_FR,
            cls.LANGUAGE_IT,
            cls.LANGUAGE_RU,
        ]

    @classmethod
    @property
    def all_foreign_advanced(cls) -> typing.List['SubjectNames']:
        return [
            cls.LANGUAGE_DE_ADVANCED,
            cls.LANGUAGE_EN_ADVANCED,
            cls.LANGUAGE_ES_ADVANCED,
            cls.LANGUAGE_FR_ADVANCED,
            cls.LANGUAGE_IT_ADVANCED,
            cls.LANGUAGE_RU_ADVANCED,
        ]

    @classmethod
    @property
    def all_foreign(cls) -> typing.List['SubjectNames']:
        return [
            cls.LANGUAGE_DE_ADVANCED,
            cls.LANGUAGE_EN_ADVANCED,
            cls.LANGUAGE_ES_ADVANCED,
            cls.LANGUAGE_FR_ADVANCED,
            cls.LANGUAGE_IT_ADVANCED,
            cls.LANGUAGE_RU_ADVANCED,
            cls.LANGUAGE_DE,
            cls.LANGUAGE_EN,
            cls.LANGUAGE_ES,
            cls.LANGUAGE_FR,
            cls.LANGUAGE_IT,
            cls.LANGUAGE_RU,
        ]
