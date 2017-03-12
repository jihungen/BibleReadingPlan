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
else
  echo "Please use the following DB options:"
  echo "kor_new, kor_rev, eng_niv"
  exit 1
fi

echo "Building e-book with HTML files..."
cd ./ebook
python3 ../../ebookmaker/ebookmaker.py oyb_chronogical_order.json
cd ../
mv ./ebook/oyb_chronogical_order.epub ./oyb_${2}_${1}.epub
