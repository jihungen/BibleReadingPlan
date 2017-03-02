import sqlite3
from bible import BibleDescription

class DBBook(object):
    '''Transform book fullname to the table (book) in DB'''
    book_fullname_to_db = {
    	'GENESIS': 'Genesis',
    	'EXODUS': 'Exodus',
    	'LEVITICUS': 'Leviticus',
    	'NUMBERS': 'Numbers',
    	'DEUTERONOMY': 'Deuteronomy',
    	'JOSHUA': 'Joshua',
    	'JUDGES': 'Judges',
    	'RUTH': 'Ruth',
    	'1 SAMUEL': 'FirstSamuel',
    	'2 SAMUEL': 'SecondSamuel',
    	'1 KINGS': 'FirstKings',
    	'2 KINGS': 'SecondKings',
    	'1 CHRONICLES': 'FirstChronicles',
    	'2 CHRONICLES': 'SecondChronicles',
    	'EZRA': 'Ezra',
    	'NEHEMIAH': 'Nehemiah',
    	'ESTHER': 'Esther',
    	'JOB': 'Job',
    	'PSALM': 'Psalms',
    	'PROVERBS': 'Proverbs',
    	'ECCLESIASTES': 'Ecclesiastes',
    	'SONG': 'SongOfSongs',
    	'ISAIAH': 'Isaiah',
    	'JEREMIAH': 'Jeremiah',
    	'LAMENTATIONS': 'Lamentations',
    	'EZEKIEL': 'Ezekiel',
    	'DANIEL': 'Daniel',
    	'HOSEA': 'Hosea',
    	'JOEL': 'Joel',
    	'AMOS': 'Amos',
    	'OBADIAH': 'Obadiah',
    	'JONAH': 'Jonah',
    	'MICAH': 'Micah',
    	'NAHUM': 'Nahum',
    	'HABAKKUK': 'Habakkuk',
    	'ZEPHANIAH': 'Zephaniah',
    	'HAGGAI': 'Haggai',
    	'ZECHARIAH': 'Zechariah',
    	'MALACHI': 'Malachi',
    	'MATTHEW': 'Matthew',
    	'MARK': 'Mark',
    	'LUKE': 'Luke',
    	'JOHN': 'John',
    	'ACTS': 'Acts',
    	'ROMANS': 'Romans',
    	'1 CORINTHIANS': 'FirstCorinthians',
    	'2 CORINTHIANS': 'SecondCorinthians',
    	'GALATIANS': 'Galatians',
    	'EPHESIANS': 'Ephesians',
    	'PHILIPPIANS': 'Philippians',
    	'COLOSSIANS': 'Colossians',
    	'1 THESSALONIANS': 'FirstThessalonians',
    	'2 THESSALONIANS': 'SecondThessalonians',
    	'1 TIMOTHY': 'FirstTimothy',
    	'2 TIMOTHY': 'SecondTimothy',
    	'TITUS': 'Titus',
    	'PHILEMON': 'Philemon',
    	'HEBREWS': 'Hebrews',
    	'JAMES': 'James',
    	'1 PETER': 'FirstPeter',
    	'2 PETER': 'SecondPeter',
    	'1 JOHN': 'FirstJohn',
    	'2 JOHN': 'SecondJohn',
    	'3 JOHN': 'ThirdJohn',
    	'JUDE': 'Jude',
    	'REVELATION': 'Revelation'
    }

    @classmethod
    def get_db_book(cls, book_fullname):
        if book_fullname not in cls.book_fullname_to_db.keys():
            return None

        return cls.book_fullname_to_db[book_fullname]

class Execution(object):
    '''Execute the query with given bible information'''
    INDEX_CHAPTER = 1
    INDEX_VERSE = 2
    INDEX_TYPE = 4
    INDEX_TEXT = 5

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_text(self, bible):
        db_book = DBBook.get_db_book(bible.book)
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

            if chapter == bible.from_chapter and verse < bible.from_verse or \
                chapter == bible.to_chapter and verse > bible.to_verse:
                continue

            results.append(curr)

        return results

    def close_connection(self):
        self.conn.close()
