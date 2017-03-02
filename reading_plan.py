#-*- coding: utf-8 -*-
import re
from bible import BibleDescription
from db_connector import Execution

DATE_KEYWORD = 'Readings'

MONTH_PATTERN_STR = '[A-Z][a-z]+'
DAY_PATTERN_STR = '[0-9]+'
DATE_PATTERN_STR = MONTH_PATTERN_STR + ' ' + DAY_PATTERN_STR

date_pattern = re.compile(DATE_PATTERN_STR)
month_pattern = re.compile(MONTH_PATTERN_STR)
day_pattern = re.compile(DAY_PATTERN_STR)

def extract_date(str):
    date_str = date_pattern.findall(str)
    if not date_str:
        return None, None

    month = month_pattern.findall(date_str[0])[0]
    day = day_pattern.findall(date_str[0])[0]
    return month, day

db_exec = Execution("./resources/Korean_NewTrans.db")

input_file = open("./resources/bible_reading_plan.txt", "r")
lines = input_file.readlines()
for line in lines:
    if DATE_KEYWORD in line:
        month, day = extract_date(line)
        if month and day:
            pass
    else:
        print line
        bible = BibleDescription(line)
        bible_text = db_exec.get_text(bible)
        last_chapter = 0

        for curr in bible_text:
            chapter = curr[Execution.INDEX_CHAPTER]
            verse = curr[Execution.INDEX_VERSE]
            content_type = curr[Execution.INDEX_TYPE]
            text = curr[Execution.INDEX_TEXT]

            if chapter != last_chapter:
                print bible.book + u' ' + str(chapter) + u'장'
                last_chapter = chapter

            if content_type == 1:
                print str(verse) + '. ' + text
            else:
                print text

input_file.close()
db_exec.close_connection()
