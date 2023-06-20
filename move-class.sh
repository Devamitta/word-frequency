cd "/home/deva/Documents/dps/scripts"

bash push-sbs-pd.sh

bash push-ru.sh

cp -f "/home/deva/Documents/Docs/SBS/analysis-of-sbs-pāli-english-recitations.pdf" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/analysis-of-sbs-pali-english-recitations.pdf"

cp -f "/home/deva/Documents/Docs/SBS/analysis-of-sbs-pāli-english-recitations.pdf" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/SBS Pāli-English Recitations/analysis-of-sbs-pāli-english-recitations.pdf"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-20.06.2023_13-45-06' temp-push/analysis-of-sbs-pali-english-recitations.pdf

echo "analysis on the GitHub - done"

cd "/home/deva/Downloads"

cp -f "Vocab Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Vocab Pāli Class.apkg"

mv -f "Vocab Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Vocab Pāli Class.apkg"

cp -f "Grammar Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Grammar Pāli Class.apkg"

mv -f "Grammar Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Grammar Pāli Class.apkg"

cp -f "Roots Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Roots Class.apkg"

mv -f "Roots Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Roots Class.apkg"

cp -f "Phonetic Changes Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Phonetic Changes Pāli Class.apkg"

mv -f "Phonetic Changes Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Phonetic Changes Pāli Class.apkg"

cp -f "Common Roots Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Common Roots Pāli Class.apkg"

mv -f "Common Roots Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Common Roots Pāli Class.apkg"


echo "all apkg - done"

cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"

cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

echo "all vocab.xlsx - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/classes" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

echo "all csv for anki - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/grammar" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

cp -f "/home/deva/Documents/dps/csv-for-anki/abbr.xlsx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/abbreviations.xlsx"

cp -f "/home/deva/Documents/dps/test.md" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/class-test.md"

# echo "making wordtree"

# cd "/home/deva/Documents/dps/word-frequency/"

# bash wordtree-for-all-class.sh

# echo "wordtree cleaning"

# cd "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/wordtree"

# find . -wholename './class1/*' | xargs rm -rf
# find . -wholename './class2/*' | xargs rm -rf
# find . -wholename './class3/*' | xargs rm -rf
# find . -wholename './class4/*' | xargs rm -rf
# find . -wholename './class5/*' | xargs rm -rf
# find . -wholename './class6/*' | xargs rm -rf
# find . -wholename './class7/*' | xargs rm -rf
# find . -wholename './class8/*' | xargs rm -rf
# find . -wholename './class9/*' | xargs rm -rf
# find . -wholename './class10/*' | xargs rm -rf
# find . -wholename './class11/*' | xargs rm -rf
# find . -wholename './class12/*' | xargs rm -rf
# find . -wholename './class13/*' | xargs rm -rf
# find . -wholename './class14/*' | xargs rm -rf

# cd "/home/deva/Documents/sasanarakkha/study-tools/pali-class/wordtree"

# find . -wholename './class1/*' | xargs rm -rf
# find . -wholename './class2/*' | xargs rm -rf
# find . -wholename './class3/*' | xargs rm -rf
# find . -wholename './class4/*' | xargs rm -rf
# find . -wholename './class5/*' | xargs rm -rf
# find . -wholename './class6/*' | xargs rm -rf
# find . -wholename './class7/*' | xargs rm -rf
# find . -wholename './class8/*' | xargs rm -rf
# find . -wholename './class9/*' | xargs rm -rf
# find . -wholename './class10/*' | xargs rm -rf
# find . -wholename './class11/*' | xargs rm -rf
# find . -wholename './class12/*' | xargs rm -rf
# find . -wholename './class13/*' | xargs rm -rf
# find . -wholename './class14/*' | xargs rm -rf


# cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

# cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"


# echo "all pics-wordtree - done"

echo "all done - new class updated"

cd "/home/deva/Documents"

code sbs.code-workspace


