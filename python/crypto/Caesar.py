# -*- coding: utf-8 -*-
"""
Caesar Encrypt & Decrypt

Support: Vietnamese language, number, special symbol

@author: Johto Robbie
"""

import sys, argparse

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialcase = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
vncase = ['À', 'Á', 'Â', 'Ã', 'È', 'É', 'Ê', 'Ì', 'Í', 'Ò', 'Ó', 'Ô', 'Õ', 'Ù', 'Ú', 'Ý', 'à', 'á', 'â', 'ã', 'è', 'é', 'ê', 'ì', 'í', 'ò', 'ó', 'ô', 'õ', 'ù', 'ú', 'ý', 'Ă', 'ă', 'Đ', 'đ', 'Ĩ', 'ĩ', 'Ũ', 'ũ', 'Ơ', 'ơ', 'Ư', 'ư', 'Ạ', 'ạ', 'Ả', 'ả', 'Ấ', 'ấ', 'Ầ', 'ầ', 'Ẩ', 'ẩ', 'Ẫ', 'ẫ', 'Ậ', 'ậ', 'Ắ', 'ắ', 'Ằ', 'ằ', 'Ẳ', 'ẳ', 'Ẵ', 'ẵ', 'Ặ', 'ặ', 'Ẹ', 'ẹ', 'Ẻ', 'ẻ', 'Ẽ', 'ẽ', 'Ế', 'ế', 'Ề', 'ề', 'Ể', 'ể', 'Ễ', 'ễ', 'Ệ', 'ệ', 'Ỉ', 'ỉ', 'Ị', 'ị', 'Ọ', 'ọ', 'Ỏ', 'ỏ', 'Ố', 'ố', 'Ồ', 'ồ', 'Ổ', 'ổ', 'Ỗ', 'ỗ', 'Ộ', 'ộ', 'Ớ', 'ớ', 'Ờ', 'ờ', 'Ở', 'ở', 'Ỡ', 'ỡ', 'Ợ', 'ợ', 'Ụ', 'ụ', 'Ủ', 'ủ', 'Ứ', 'ứ', 'Ừ', 'ừ', 'Ử', 'ử', 'Ữ', 'ữ', 'Ự', 'ự', 'Ỳ', 'ỳ', 'Ỵ', 'ỵ', 'Ỷ', 'ỷ', 'Ỹ', 'ỹ']

def listToString(listinput): 
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in listinput: 
        str1 += ele  
    
    # return string  
    return str1

def caesarEncrypt(realText, step):
	outText = []
	cryptText = []

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		elif eachLetter in specialcase:
			index = specialcase.index(eachLetter)
			crypting = (index + step) % 41
			cryptText.append(crypting)
			newLetter = specialcase[crypting]
			outText.append(newLetter)
		elif eachLetter in vncase:
			index = vncase.index(eachLetter)
			crypting = (index + step) % 134
			cryptText.append(crypting)
			newLetter = vncase[crypting]
			outText.append(newLetter)
		else:
		    outText.append(eachLetter)
	return outText
	
def caesarDecrypt(realText, step):
	outText = []
	cryptText = []

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index - step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index - step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		elif eachLetter in specialcase:
			index = specialcase.index(eachLetter)
			crypting = (index - step) % 41
			cryptText.append(crypting)
			newLetter = specialcase[crypting]
			outText.append(newLetter)
		elif eachLetter in vncase:
			index = vncase.index(eachLetter)
			crypting = (index - step) % 134
			cryptText.append(crypting)
			newLetter = vncase[crypting]
			outText.append(newLetter)
		else:
		    outText.append(eachLetter)
	return outText
    

def main():
    msg = ""
    pwd = ""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", help="Choose encrypt mode or decrypt mode", \
                        choices=["e", "encode", "d", "decode"])
    args = parser.parse_args()
    
    if args.mode == "e" or args.mode == "encrypt":
        msg = input('Message...: ')
        pwd = input('Password..: ')
        print(listToString(caesarEncrypt(msg, len(pwd))))
    elif args.mode == "d" or args.mode == "decrypt":
        msg = input('Message...: ')
        pwd = input('Password..: ')
        print(listToString(caesarDecrypt(msg, len(pwd))))
    else:
        print("python caesar.py --help                     - show this help message")
        sys.exit()


if __name__ == "__main__":
    main()
