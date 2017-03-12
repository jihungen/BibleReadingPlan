#-*- coding: utf-8 -*-
import re
import codecs
from sys import argv
from datetime import datetime, timedelta

from bible import Date, BibleDay, BibleDescription
from db_connector import Execution
from epub import HTMLForm

script, datetime_str, db_path = argv

print script, datetime_str, db_path
datetime_obj = datetime.strptime(datetime_str, '%Y%m%d')

DATE_KEYWORD = 'Readings'

# db_exec = Execution("./resources/Korean_NewTrans.db")
db_exec = Execution(db_path)

bible_day_list = []
bible_day = None

input_file = open("./resources/bible_reading_plan.txt", "r")
lines = input_file.readlines()
for line in lines:
    if DATE_KEYWORD in line:
        if bible_day:
            bible_day_list.append(bible_day)
            bible_day = None

        bible_day = BibleDay(datetime_obj.year, datetime_obj.month, datetime_obj.day)
        datetime_obj += timedelta(days=1)

    else:
        bible = BibleDescription(line)

        if not bible.is_empty():
            text_list = db_exec.get_text(bible)
            bible.add_text_list(text_list)
            bible_day.add_bible_desc(bible)

if bible_day:
    bible_day_list.append(bible_day)

input_file.close()
db_exec.close_connection()

for curr_bible_day in bible_day_list:
    output_file = codecs.open("./ebook/" + curr_bible_day.get_filename(), "w", "utf-8")
    content = HTMLForm.generateHTML(curr_bible_day.get_date_str(), curr_bible_day.bible_desc_list)
    output_file.write(content)
    output_file.close()
