tesseract a.jpg stdout -l eng --psm 13 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test2.jpg stdout -l eng --psm 13 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test2.jpg stdout -l eng --psm 12 -c tessedit_char_whitelist="0123456789+-xX?="

tesseract b.jpg stdout -l eng --psm 13 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test3.jpg stdout -l eng --psm 13 -c tessedit_char_whitelist="4X8=?"
tesseract test4.jpg stdout -l eng --psm 13 -c tessedit_char_whitelist="4X8=?"
tesseract test4.gif stdout -l eng --psm 13 -c tessedit_char_whitelist="4X8=?"
tesseract yzm.gif stdout -l eng --oem 0 --psm 13 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test4.gif stdout -l eng --psm 13 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test3.jpg stdout -l eng --psm 12 -c tessedit_char_whitelist="0123456789+-xX?="
tesseract test3.jpg stdout -l eng --psm 11 -c tessedit_char_whitelist="0123456789+-xX?="

convert b.jpg -crop 88x23+1+1! -threshold 50%  test5.gif
