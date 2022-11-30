
# clean folders before

cd "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree"

find . -wholename './class1/*' | xargs rm -rf
find . -wholename './class2/*' | xargs rm -rf
find . -wholename './class3/*' | xargs rm -rf
find . -wholename './class4/*' | xargs rm -rf
find . -wholename './class5/*' | xargs rm -rf
# find . -wholename './class6/*' | xargs rm -rf
# find . -wholename './class7/*' | xargs rm -rf
# find . -wholename './class8/*' | xargs rm -rf
# find . -wholename './class9/*' | xargs rm -rf
# find . -wholename './class10/*' | xargs rm -rf
# find . -wholename './class11/*' | xargs rm -rf
# find . -wholename './class12/*' | xargs rm -rf
# find . -wholename './class13/*' | xargs rm -rf
# find . -wholename './class14/*' | xargs rm -rf

# generate wordtree for all classes

cd "/home/deva/Documents/dps/word-frequency"

python3 wordtree-pali.py 1
python3 wordtree-pali.py 2
python3 wordtree-pali.py 3
python3 wordtree-pali.py 4
python3 wordtree-pali.py 5
# python3 wordtree-pali.py 6
# python3 wordtree-pali.py 7
# python3 wordtree-pali.py 8
# python3 wordtree-pali.py 9
# python3 wordtree-pali.py 10
# python3 wordtree-pali.py 11
# python3 wordtree-pali.py 12
# python3 wordtree-pali.py 13
# python3 wordtree-pali.py 14

# separate png

cd "/home/deva/Documents/dps/word-frequency/pics-wordtree"

find . -wholename './class1/*.png' -exec mv {} ./wordtree/class1 \;
find . -wholename './class2/*.png' -exec mv {} ./wordtree/class2 \;
find . -wholename './class3/*.png' -exec mv {} ./wordtree/class3 \;
find . -wholename './class4/*.png' -exec mv {} ./wordtree/class4 \;
find . -wholename './class5/*.png' -exec mv {} ./wordtree/class5 \;
# find . -wholename './class6/*.png' -exec mv {} ./wordtree/class6 \;
# find . -wholename './class7/*.png' -exec mv {} ./wordtree/class7 \;
# find . -wholename './class8/*.png' -exec mv {} ./wordtree/class8 \;
# find . -wholename './class9/*.png' -exec mv {} ./wordtree/class9 \;
# find . -wholename './class10/*.png' -exec mv {} ./wordtree/class10 \;
# find . -wholename './class11/*.png' -exec mv {} ./wordtree/class11 \;
# find . -wholename './class12/*.png' -exec mv {} ./wordtree/class12 \;
# find . -wholename './class13/*.png' -exec mv {} ./wordtree/class13 \;
# find . -wholename './class14/*.png' -exec mv {} ./wordtree/class14 \;

