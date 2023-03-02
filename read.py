# import pdf processor PyPDF2
import PyPDF2

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os

import socket 

# get name of file

file = input("file path name: ")

# check if file exist
print("checking if pdf exists ...")

if os.path.exists(file + ".pdf") == False:

    print(f"error!! pdf with name {file} doesn't exist. ")
    print(f"try copy and pasting an existing pdf file name without '.pdf'.")
    print(f"exiting...")
    exit(0)

elif os.path.getsize(file + ".pdf") == False:
    print(f"error!! pdf with name {file} is empty. ")
    print(f"try another existing pdf file name . ")
    exit(0)



# path of the PDF file
print(f"opening {file} ...")

path = open(file + ".pdf", 'rb')


# creating a PdfFileReader object
print(f"reading {file} ...")
pdfReader = PyPDF2.PdfReader(path)

# Function to convert a list to a string


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

# count total number of pages
print(f"counting pages in {file} ...")

totalPages = int(len(pdfReader.pages))

# create an array to store the text

mytext = []

# get number of page to print from user
# verifying inputs

xi = input("input start page: ")
if xi.isdigit() == False:
    print(f"start page can't be empty, negative nor text. input digit only. exiting...")
    exit(0)
x = int(xi)
if x<=0 :
    print(f"start page can't be zero, negative. input digit only. exiting...")
    exit(0)
yi = input("input end page: ")
if yi.isdigit() == False:
    print(f"end page cant be empty, negative nor text. input digit only.  exiting...")
    exit(0)
y = int(yi)
if y<=0:
    print(f"end page cant be zero nor negative exiting...")
    exit(0)

# verify the input
print(f"calculating and analyzing start and end page {x} to {y} ...")

if x>y:
    print(f"start page can't be greater than end page {x}>{y} hence exiting...")
    exit(0)

elif x>totalPages or y>totalPages:
    print(f"start page or end page can't be greater than the total pages: {totalPages} exiting...")
    exit(0)

elif x==y:
# this will make only the page inserted
# extracting the text from the PDF
# The text that you want to convert to audio
    print(f"extracting text from page {x} in {file} pdf ...")

    from_page = pdfReader.pages[x-1]

    mytext = from_page.extract_text()
else:
# this will loop over the page inserted
# and assign the value to from_page
    print(f"extracting text from page {x} to {y} in {file} pdf ...")

    for num in range(x, y):
      from_page = pdfReader.pages[num-1]

# extracting the text from the PDF
# The text that you want to convert to audio
# and assigning values to correspoding array
      mytext.append(from_page.extract_text())

# converting the array to text
    mytext = listToString(mytext)
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
print(f"converting {file} pdf to audio {file} mp3 ...")

myobj = gTTS(text=mytext, lang=language, slow=False, tld='us')
  
# Saving the converted audio in a mp3 file named
# for the name inputted
print(f"saving {file}.pdf as {file}.mp3")


file_audio = file + ".mp3"
myobj.save(file_audio)

if os.path.getsize(file + ".mp3") == 0 or os.path.exists(file + ".mp3") == False:
    print("something went wrong!! Network error occured")
    print(f"failed to save {file}.mp3")
    print("You can try reconverting in a good network environment")
    print("exiting...")
    exit(0)



# Affirm end of program

print(f" DONE")
print(f"filename: {file}.mp3")
print(f"Want to convert more file ? ")
print(f"you can simply rerun the program...")























