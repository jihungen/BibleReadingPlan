#!/bin/bash
#$1: 20170312
#$2: ./resources/Korean_NewTrans.db
echo "Starting date: $1"
echo "Bible translation: $2"

rm ./ebook/bible_*
rm ./ebook/oyb_chronogical_order.epub

echo "Building HTML files for e-book..."
if [ $2 = "kor_new" ]
then
  python reading_plan.py ${1} ./resources/Korean_NewTrans.db
elif [ $2 = "kor_rev" ]
then
  python reading_plan.py ${1} ./resources/Korean_Revised.db
elif [ $2 = "eng_niv" ]
then
  python reading_plan.py ${1} ./resources/NIV2011.db
elif [ $2 = "kor_easy" ]
then
  python reading_plan.py ${1} ./resources/EasyBible.db
else
  echo "Please use the following DB options:"
  echo "kor_new, kor_rev, kor_easy, eng_niv"
  exit 1
fi

echo "Building e-book with HTML files..."
cd ./ebook

if [ $2 = "kor_new" ]
then
  python3 ../../ebookmaker/ebookmaker.py oyb_cover_kor_new.json
elif [ $2 = "kor_rev" ]
then
  python3 ../../ebookmaker/ebookmaker.py oyb_cover_kor_rev.json
elif [ $2 = "eng_niv" ]
then
  python3 ../../ebookmaker/ebookmaker.py oyb_cover_eng_niv.json
elif [ $2 = "kor_easy" ]
then
  python3 ../../ebookmaker/ebookmaker.py oyb_cover_kor_easy.json
else
  echo "Please use the following DB options:"
  echo "kor_new, kor_rev, kor_easy, eng_niv"
  exit 1
fi

cd ../

if [ $2 = "kor_new" ]
then
  mv ./ebook/oyb_cover_kor_new.epub ./oyb_${2}_${1}.epub
elif [ $2 = "kor_rev" ]
then
  mv ./ebook/oyb_cover_kor_rev.epub ./oyb_${2}_${1}.epub
elif [ $2 = "eng_niv" ]
then
  mv ./ebook/oyb_cover_eng_niv.epub ./oyb_${2}_${1}.epub
elif [ $2 = "kor_easy" ]
then
  mv ./ebook/oyb_cover_kor_easy.epub ./oyb_${2}_${1}.epub
else
  echo "Please use the following DB options:"
  echo "kor_new, kor_rev, kor_easy, eng_niv"
  exit 1
fi

#rm ./ebook/bible_*.html
