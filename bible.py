# -*- coding: utf-8 -*-
import re

BOOK_PATTERN_STR = '[0-9]?[ ]?[A-Z]+'
BIBLE_RANGE_PATTERN_STR = '[0-9]+\:[0-9|\-|\:]*[0-9]+'
BIBLE_DESC_PATTERN_STR = BOOK_PATTERN_STR + ' ' + BIBLE_RANGE_PATTERN_STR

bible_desc_pattern = re.compile(BIBLE_DESC_PATTERN_STR)
book_pattern = re.compile(BOOK_PATTERN_STR)
bible_range_pattern = re.compile(BIBLE_RANGE_PATTERN_STR)

class BibleDescription(object):
    book = None
    from_chapter = to_chapter = from_verse = to_verse = 0

    def __init__(self, bible_desc):
        found_str = bible_desc_pattern.findall(bible_desc)
        if not found_str or len(found_str[0]) <= 0:
            return

        self.book = book_pattern.findall(found_str[0])[0]
        bible_range = bible_range_pattern.findall(found_str[0])[0]
        self.from_chapter, self.from_verse, self.to_chapter, self.to_verse = BibleDescription.parse_range(bible_range)

    def add_text(self, text):
        self.text

    def print_info(self):
        print self.book + ' ' + self.from_chapter + ':' + self.from_verse + ' to ' + self.to_chapter + ':' + self.to_verse
        print str(self.text)

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
