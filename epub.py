# -*- coding: utf-8 -*-
from bible import BibleDescription
from book import Book
from db_connector import Execution

class HTMLForm(object):
    PRE_HEAD = u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>'''

    POST_HEAD = u'''</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="style.css" type="text/css" />
    </head>
    '''

    PRE_BODY = u'<body>\n'
    POST_BODY = u'</body>\n</html>\n'

    @classmethod
    def generateHTMLHead(cls, title):
        print u'title: ' + title
        return cls.PRE_HEAD + title + cls.POST_HEAD

    @classmethod
    def generateHTMLDateHead(cls, date_str):
        print u'date_str: ' + date_str
        return u'<h1>' + date_str + u'</h1>\n'

    @classmethod
    def generateHTMLBibleHead(cls, bible_info):
        print u'bible_info: ' + bible_info
        return u'<h2>' + bible_info + u'</h2>\n'

    @classmethod
    def generateHTMLBibleChapterHead(cls, bible_chapter_info):
        print u'bible_chapter_info: ' + bible_chapter_info
        return u'<h3>' + bible_chapter_info + u'</h3>\n'

    @classmethod
    def generateHTMLBibleText(cls, bible_text):
        # print u'bible_text: ' + bible_text
        return u'<p>' + bible_text + u'<p>\n'

    @classmethod
    def generateHTML(cls, date_str, bible_desc_list):
        content = HTMLForm.generateHTMLHead(date_str)
        content += HTMLForm.PRE_BODY
        content += HTMLForm.generateHTMLDateHead(date_str)

        for bible_desc in bible_desc_list:
            content += HTMLForm.generateHTMLBibleHead(bible_desc.get_info())

            last_chapter = 0
            for curr_text in bible_desc.text_list:
                chapter = curr_text[Execution.INDEX_CHAPTER]
                verse = curr_text[Execution.INDEX_VERSE]
                bible_text = curr_text[Execution.INDEX_TEXT]

                if bible_desc.has_multiple_chapters() and chapter != last_chapter:
                    content += HTMLForm.generateHTMLBibleChapterHead(Book.get_korean_book(bible_desc.book) + u' ' + str(chapter) + u'장')
                    last_chapter = chapter

                show_text = bible_text
                if curr_text[Execution.INDEX_TYPE] == 1:
                    show_text = str(verse) + '. ' + show_text

                content += HTMLForm.generateHTMLBibleText(show_text)

        content += HTMLForm.POST_BODY
        return content
