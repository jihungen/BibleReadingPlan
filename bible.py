# -*- coding: utf-8 -*-
import re
from book import Book

class Date(object):
    MONTH_PATTERN_STR = '[A-Z][a-z]+'
    DAY_PATTERN_STR = '[0-9]+'
    DATE_PATTERN_STR = MONTH_PATTERN_STR + ' ' + DAY_PATTERN_STR

    date_pattern = re.compile(DATE_PATTERN_STR)
    month_pattern = re.compile(MONTH_PATTERN_STR)
    day_pattern = re.compile(DAY_PATTERN_STR)

    month_to_numeber = {
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5
    }

    @classmethod
    def get_month_number(cls, month):
        if month not in cls.month_to_numeber.keys():
            return -1

        return cls.month_to_numeber[month]

    @classmethod
    def extract_date(cls, str):
        date_str = cls.date_pattern.findall(str)
        if not date_str:
            return None, None

        month = cls.month_pattern.findall(date_str[0])[0]
        day = cls.day_pattern.findall(date_str[0])[0]
        return month, int(day)

class BibleDay:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.bible_desc_list = []

    def add_bible_desc(self, bible_desc):
        self.bible_desc_list.append(bible_desc)

    def get_date_str(self):
        return str(self.year) + u'년 ' + str(self.month) + u'월 ' + str(self.day) + u'일'

    def get_filename(self):
        return 'bible_' + str(self.year) + '%02d' % self.month + '%02d' % self.day + '.html'

class BibleDescription:
    BOOK_PATTERN_STR = '[0-9]?[ ]?[A-Z]+'
    BIBLE_RANGE_PATTERN_STR = '[0-9]+\:[0-9|\-|\:]*[0-9]+'
    BIBLE_DESC_PATTERN_STR = BOOK_PATTERN_STR + ' ' + BIBLE_RANGE_PATTERN_STR

    bible_desc_pattern = re.compile(BIBLE_DESC_PATTERN_STR)
    book_pattern = re.compile(BOOK_PATTERN_STR)
    bible_range_pattern = re.compile(BIBLE_RANGE_PATTERN_STR)

    def __init__(self, bible_desc):
        found_str = BibleDescription.bible_desc_pattern.findall(bible_desc)
        if not found_str or len(found_str[0]) <= 0:
            self.book = None
            return

        self.book = BibleDescription.book_pattern.findall(found_str[0])[0]
        bible_range = BibleDescription.bible_range_pattern.findall(found_str[0])[0]
        self.from_chapter, self.from_verse, self.to_chapter, self.to_verse = BibleDescription.parse_range(bible_range)
        self.text_list = []

    def is_empty(self):
        return self.book == None

    def has_multiple_chapters(self):
        return self.from_chapter != self.to_chapter

    def add_text_list(self, text_list):
        self.text_list.extend(text_list)

    def get_info(self):
        content = Book.get_korean_book(self.book) + ' ' + str(self.from_chapter) + ':' + str(self.from_verse)
        if self.has_multiple_chapters():
            content += '-' + str(self.to_chapter) + ':' + str(self.to_verse)
        elif self.from_verse != self.to_verse:
            content += '-' + str(self.to_verse)
        return content

    @staticmethod
    def parse_range(bible_range):
        from_chapter = from_verse = to_chapter = to_verse = None
        range_count = bible_range.count(':')

        if range_count == 2:
            ranges = bible_range.split('-')
            if ranges and len(ranges) == 2:
                from_chapter, from_verse = BibleDescription.parse_single_range(ranges[0])
                to_chapter, to_verse = BibleDescription.parse_single_range(ranges[1])
        elif range_count == 1:
            from_chapter, verse_range = BibleDescription.parse_single_range(bible_range)
            to_chapter = from_chapter

            verse_content = verse_range.split('-')
            if verse_content and len(verse_content) == 2:
                from_verse = verse_content[0]
                to_verse = verse_content[1]
            else:
                from_verse = verse_range
                to_verse = verse_range

        return int(from_chapter), int(from_verse), int(to_chapter), int(to_verse)

    @staticmethod
    def parse_single_range(bible_range):
        content = bible_range.split(':')
        if not content or len(content) != 2:
            return None, None

        return content[0], content[1]
