import sqlite3
from bible import BibleDescription
from book import Book

class Execution(object):
    '''Execute the query with given bible information'''
    INDEX_CHAPTER = 1
    INDEX_VERSE = 2
    INDEX_DIVIDED_VERSE = 3
    INDEX_TYPE = 4
    INDEX_TEXT = 5

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_text(self, bible):
        db_book = Book.get_db_book(bible.book)
        if db_book is None:
            return {}

        chapter_list = range(bible.from_chapter, bible.to_chapter + 1)
        self.cursor.execute('''SELECT * FROM %(book)s
            WHERE chapter IN (%(chapters)s)
            ORDER BY chapter ASC, verse ASC, verseIdx ASC''' % {
                'book': db_book,
                'chapters': ', '.join(str(x) for x in chapter_list)}
        )

        results = []
        for curr in self.cursor:
            chapter = curr[Execution.INDEX_CHAPTER]
            verse = curr[Execution.INDEX_VERSE]
            text = curr[Execution.INDEX_TEXT]

            if chapter == bible.from_chapter and (bible.from_verse > 0 and verse < bible.from_verse) or \
                chapter == bible.to_chapter and (bible.to_verse > 0 and verse > bible.to_verse):
                continue

            results.append(curr)

        return results

    def close_connection(self):
        self.conn.close()
