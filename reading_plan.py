#-*- coding: utf-8 -*-
import re
import codecs
from bible import Date, BibleDay, BibleDescription
from db_connector import Execution
from epub import HTMLForm

DATE_KEYWORD = 'Readings'

db_exec = Execution("./resources/Korean_NewTrans.db")

year = 2016
bible_day_list = []
bible_day = None

input_file = open("./input/bible_reading_plan.txt", "r")
lines = input_file.readlines()
for line in lines:
    if DATE_KEYWORD in line:
        month, day = Date.extract_date(line)
        if bible_day:
            bible_day_list.append(bible_day)
            bible_day = None

        bible_day = BibleDay(month, day)

    else:
        bible = BibleDescription(line)

        if not bible.is_empty():
            print bible.book

            text_list = db_exec.get_text(bible)
            bible.add_text_list(text_list)
            bible_day.add_bible_desc(bible)
            print line

if bible_day:
    bible_day_list.append(bible_day)

input_file.close()
db_exec.close_connection()

b_increased_year = False
for curr_bible_day in bible_day_list:
    if curr_bible_day.month == 1 and not b_increased_year:
        year += 1
        b_increased_year = True

    output_file = codecs.open("./output/" + curr_bible_day.get_filename(year), "w", "utf-8")
    content = HTMLForm.generateHTML(curr_bible_day.get_date_str(), curr_bible_day.bible_desc_list)
    output_file.write(content)
    output_file.close()
