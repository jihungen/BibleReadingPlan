# -*- coding: utf-8 -*-
class Book(object):
    '''Transform book fullname to the table (book) in DB'''
    
    INDEX_KOREAN = 0
    INDEX_DB = 1

    book_fullnames = {
    	'GENESIS': (u'창세기','Genesis'),
    	'EXODUS': (u'출애굽기','Exodus'),
    	'LEVITICUS': (u'레위기','Leviticus'),
    	'NUMBERS': (u'민수기','Numbers'),
    	'DEUTERONOMY': (u'신명기','Deuteronomy'),
    	'JOSHUA': (u'여호수아','Joshua'),
    	'JUDGES': (u'사사기','Judges'),
    	'RUTH': (u'룻기','Ruth'),
    	'1 SAMUEL': (u'사무엘상','FirstSamuel'),
    	'2 SAMUEL': (u'사무엘하','SecondSamuel'),
    	'1 KINGS': (u'열왕기상','FirstKings'),
    	'2 KINGS': (u'열왕기하','SecondKings'),
    	'1 CHRONICLES': (u'역대상','FirstChronicles'),
    	'2 CHRONICLES': (u'역대하','SecondChronicles'),
    	'EZRA': (u'에스라','Ezra'),
    	'NEHEMIAH': (u'느헤미야','Nehemiah'),
    	'ESTHER': (u'에스더','Esther'),
    	'JOB': (u'욥기','Job'),
    	'PSALM': (u'시편','Psalms'),
    	'PROVERBS': (u'잠언','Proverbs'),
    	'ECCLESIASTES': (u'전도서','Ecclesiastes'),
    	'SONG': (u'아가','SongOfSongs'),
    	'ISAIAH': (u'이사야','Isaiah'),
    	'JEREMIAH': (u'예레미야','Jeremiah'),
    	'LAMENTATIONS': (u'예레미야애가','Lamentations'),
    	'EZEKIEL': (u'에스겔','Ezekiel'),
    	'DANIEL': (u'다니엘','Daniel'),
    	'HOSEA': (u'호세아','Hosea'),
    	'JOEL': (u'요엘','Joel'),
    	'AMOS': (u'아모스','Amos'),
    	'OBADIAH': (u'오바댜','Obadiah'),
    	'JONAH': (u'요나','Jonah'),
    	'MICAH': (u'미가','Micah'),
    	'NAHUM': (u'나훔','Nahum'),
    	'HABAKKUK': (u'하박국','Habakkuk'),
    	'ZEPHANIAH': (u'스바냐','Zephaniah'),
    	'HAGGAI': (u'학개','Haggai'),
    	'ZECHARIAH': (u'스가랴','Zechariah'),
    	'MALACHI': (u'말라기','Malachi'),
    	'MATTHEW': (u'마태복음','Matthew'),
    	'MARK': (u'마가복음','Mark'),
    	'LUKE': (u'누가복음','Luke'),
    	'JOHN': (u'요한복음','John'),
    	'ACTS': (u'사도행전','Acts'),
    	'ROMANS': (u'로마서','Romans'),
    	'1 CORINTHIANS': (u'고린도전서','FirstCorinthians'),
    	'2 CORINTHIANS': (u'고린도후서','SecondCorinthians'),
    	'GALATIANS': (u'갈라디아서','Galatians'),
    	'EPHESIANS': (u'에베소서','Ephesians'),
    	'PHILIPPIANS': (u'빌립보서','Philippians'),
    	'COLOSSIANS': (u'골로새서','Colossians'),
    	'1 THESSALONIANS': (u'데살로니가전서','FirstThessalonians'),
    	'2 THESSALONIANS': (u'데살로니가후서','SecondThessalonians'),
    	'1 TIMOTHY': (u'디모데전서','FirstTimothy'),
    	'2 TIMOTHY': (u'디모데후서','SecondTimothy'),
    	'TITUS': (u'디도서','Titus'),
    	'PHILEMON': (u'빌레몬서','Philemon'),
    	'HEBREWS': (u'히브리서','Hebrews'),
    	'JAMES': (u'야고보서','James'),
    	'1 PETER': (u'베드로전서','FirstPeter'),
    	'2 PETER': (u'베드로후서','SecondPeter'),
    	'1 JOHN': (u'요한일서','FirstJohn'),
    	'2 JOHN': (u'요한이서','SecondJohn'),
    	'3 JOHN': (u'요한삼서','ThirdJohn'),
    	'JUDE': (u'유다서','Jude'),
    	'REVELATION': (u'요한계시록','Revelation')
    }

    @classmethod
    def get_db_book(cls, book_fullname):
        if book_fullname not in cls.book_fullnames.keys():
            return None

        return cls.book_fullnames[book_fullname][cls.INDEX_DB]

    @classmethod
    def get_korean_book(cls, book_fullname):
        if book_fullname not in cls.book_fullnames.keys():
            return None

        return cls.book_fullnames[book_fullname][cls.INDEX_KOREAN]
