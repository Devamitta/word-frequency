cd "/home/deva/.local/bin/"

bash push-sbs-pd.sh

echo "sbs-pd on the sever - done"

cp -f "/home/deva/Documents/dps/exporter/share/sbs-pd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.zip"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-26.08.2022_15-24-16' temp-push/sbs-pd.zip

echo "sbs-pd on the GitHub - done"

cd "/home/deva/Downloads"

mv -f "Exercises Beginner Pāli Course.docx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Exercises Beginner Pāli Course.docx"

mv -f "SBS Beginner Pāli Course.pdf" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/SBS Beginner Pāli Course.pdf"

mv -f "Key to Exercises Beginner Pāli Course.pdf" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Key to Exercises Beginner Pāli Course.pdf"

echo "all pdf and docx - done"

mv -f "Vocab Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Vocab Pāli Class.apkg"

mv -f "Grammar Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Grammar Pāli Class.apkg"

echo "all apkg - done"

cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

echo "all vocab.xlsx - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/classes" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

echo "all csv for anki - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/grammar" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

mv -f "/home/deva/Documents/dps/csv-for-anki/abbr.xlsx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/abbr.xlsx"

cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

echo "all pics-wordtree - done"

echo "can announce - new class updated"

