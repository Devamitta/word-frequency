cd "/home/deva/.local/bin/"

bash push-sbs-pd.sh

echo "sbs-pd on the sever - done"

cp -f "/home/deva/Documents/dps/exporter/share/sbs-pd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.zip"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-08.11.2022_14-30-08' temp-push/sbs-pd.zip

cp -f "/home/deva/Documents/Docs/SBS/analysis-of-sbs-pāli-english-recitations.pdf" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/analysis-of-sbs-pāli-english-recitations.pdf"

cp -f "/home/deva/Documents/Docs/SBS/analysis-of-sbs-pāli-english-recitations.pdf" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/SBS Pāli-English Recitations/analysis-of-sbs-pāli-english-recitations.pdf"

gh release upload --clobber 'artifacts-08.11.2022_14-30-08' temp-push/analysis-of-sbs-pāli-english-recitations.pdf

echo "sbs-pd on the GitHub - done"

cd "/home/deva/Downloads"

# mv -f "Exercises Beginner Pāli Course.docx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Exercises Beginner Pāli Course.docx"

# mv -f "SBS Beginner Pāli Course.pdf" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/SBS Beginner Pāli Course.pdf"

# mv -f "Key to Exercises Beginner Pāli Course.pdf" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Key to Exercises Beginner Pāli Course.pdf"

# mv -f "Examples from Tipiṭaka Beginner Course.docx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Examples from Tipiṭaka Beginner Course.docx"

# echo "all pdf and docx - done"


cp -f "Vocab Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Vocab Pāli Class.apkg"

mv -f "Vocab Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Vocab Pāli Class.apkg"

cp -f "Grammar Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Grammar Pāli Class.apkg"

mv -f "Grammar Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Grammar Pāli Class.apkg"

echo "all apkg - done"

cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"

cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

echo "all vocab.xlsx - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/classes" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

echo "all csv for anki - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/grammar" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

cp -f "/home/deva/Documents/dps/csv-for-anki/abbr.xlsx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/abbreviations.xlsx"

cp -f "/home/deva/Documents/dps/test.md" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/class-test.md"

echo "making wordtree"

cd "/home/deva/Documents/dps/word-frequency/"

bash wordtree-for-all-class.sh

echo "wordtree cleaning"

cd "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/pics-wordtree"

find . -wholename './class1/*' | xargs rm -rf
find . -wholename './class2/*' | xargs rm -rf
find . -wholename './class3/*' | xargs rm -rf
find . -wholename './class4/*' | xargs rm -rf
find . -wholename './class5/*' | xargs rm -rf
find . -wholename './class6/*' | xargs rm -rf
find . -wholename './class7/*' | xargs rm -rf
find . -wholename './class8/*' | xargs rm -rf
find . -wholename './class9/*' | xargs rm -rf
find . -wholename './class10/*' | xargs rm -rf
find . -wholename './class11/*' | xargs rm -rf
find . -wholename './class12/*' | xargs rm -rf
find . -wholename './class13/*' | xargs rm -rf
find . -wholename './class14/*' | xargs rm -rf

cd "/home/deva/Documents/sasanarakkha/study-tools/pali-class/pics-wordtree"

find . -wholename './class1/*' | xargs rm -rf
find . -wholename './class2/*' | xargs rm -rf
find . -wholename './class3/*' | xargs rm -rf
find . -wholename './class4/*' | xargs rm -rf
find . -wholename './class5/*' | xargs rm -rf
find . -wholename './class6/*' | xargs rm -rf
find . -wholename './class7/*' | xargs rm -rf
find . -wholename './class8/*' | xargs rm -rf
find . -wholename './class9/*' | xargs rm -rf
find . -wholename './class10/*' | xargs rm -rf
find . -wholename './class11/*' | xargs rm -rf
find . -wholename './class12/*' | xargs rm -rf
find . -wholename './class13/*' | xargs rm -rf
find . -wholename './class14/*' | xargs rm -rf


cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"


echo "all pics-wordtree - done"

echo "can announce - new class updated"

