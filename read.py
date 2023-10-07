        # import pdf processor PyPDF2
import PyPDF2

        # Import the required module for text 
        # to speech conversion
from gtts import gTTS
        
        # This module is imported so that we can 
        # play the converted audio
        # for good measures
import os

import socket 




# verifying page input
def verify(xi,yi,totalPages,sp):

    if xi.isdigit() == False:
            print(f"start page can't be empty, negative nor text. input digit only. try again")
            start(sp)
            
    x = int(xi)

    if x<=0 :
            print(f"start page can't be zero, negative. input digit only. exiting try again")
            start(sp)

    if yi.isdigit() == False:
            print(f"end page cant be empty, negative nor text. input digit only.  try again")
            start(sp)
            
    y = int(yi)

    if y<=0:
            print(f"end page cant be zero nor negative. try again")
            start(sp)

    if x>y:
            print(f"start page can't be greater than end page {x}>{y} hence, try again")
            start(sp)

    if x>totalPages or y>totalPages:
            print(f"start page or end page can't be greater than the total pages: {totalPages} . try again")
            start(sp)
    return ([x,y])

def convert(text,file):
        print(f'would you like to change the audio name, or would retain {file}.mp3 ? ')
        a = input('to exit press E, to change press C or to retain press R: ')
        
        if a == 'change' or a == 'c' or a == 'C' :
            file = input('input another name for your mp3 file: ')
        #check for file 
        if os.path.exists(file + ".mp3") == True:
            while ( os.path.exists(file + ".mp3") == True ) :
                print(f'filename {file}.mp3 already exist. change now.. ')
                file = input('input another name for your mp3 file: ')
        # exiting
        if a == 'exit' or a == 'e' or a == 'E' :
            print("have a nice day, thanks for using. make sure you use the right input next time.exiting...")
            exit(0)
            
                
        
        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        print(f"converting {file} pdf to audio {file} mp3 ...")

        myobj = gTTS(text=text, lang=language, slow=False, tld='us')
        
        # Saving the converted audio in a mp3 file named
        # for the name inputted
        print(f"saving {file}.pdf as {file}.mp3")

        file_audio = file + ".mp3"
        myobj.save(file_audio)
        return file


# starting input
def start(sp):
    if sp:
        print("not getting it ?")
        re = input("e to exit, s to start over, t try again: ")
        if re == 's':
            start(0)
        elif re == 't':
            pdfToSpeech(sp)
        else:
            print("have a nice day, thanks for using. make sure you use the right input next time.exiting...")
            exit(0)
        
    i = input("Do you want to convert files now? Y/N: ") 
    if not i:
        print("have a nice day, thanks for using. make sure you add a input next time.exiting...")
        exit(0)

    elif i == 'y' or i == 'Y' or i == 'yes' or i == 'YES' or i == 'Yes':
        print("running the program get ready to input the file path")
        sp = setup()
        pdfToSpeech(sp)

    else:
        # Affirm end of program

        print("have a nice day, thanks for using. bye. exiting...")
        exit(0)

    return(0)
        # Function to convert a list to a string
 

def listToString(string):

    # initialize an empty string
    str1 = ""

            # traverse in the string
    for ele in string:
        str1 += ele

            # return string
        return str1

def setup():

        # get name of file

        file = input("file path name: ")

        # check if file exist
        print("checking if pdf exists ...")

        if os.path.exists(file + ".pdf") == False:

            print(f"error!! pdf with name {file} doesn't exist. ")
            print(f"try copy and pasting an existing pdf file name without '.pdf'.")
            print(f"Try again ...")
            start(0)

        elif os.path.getsize(file + ".pdf") == False:
            print(f"error!! pdf with name {file} is empty. ")
            print(f"try another existing pdf file name . ")
            print(f"Try again ...")
            start(0)


        # path of the PDF file
        print(f"opening {file} ...")

        path = open(file + ".pdf", 'rb')


        # creating a PdfFileReader object
        print(f"reading {file} ...")
        pdfReader = PyPDF2.PdfReader(path)

        # count total number of pages
        print(f"counting pages in {file} ...")
        
        return [pdfReader, file]

        
       
def pdfToSpeech(sp):
    
        # spliting arrays
        pdfReader = sp[0]
        file = sp[1]

        totalPages = int(len(pdfReader.pages))
        
        # create an array to store the text
        mytext = []
        print('NOTE: to print just a page input the same value for start and end page ')

        # get number of page to print from user
        # verifying inputs
        # getting input

        x = input("input start page: ")

        y = input("input end page: ")

        print(f"calculating and analyzing start and end page {x} to {y} ...")
        
        # verify the input
        j = verify(x,y,totalPages,sp)
        x = j[0]
        y = j[1]

        if x==y:
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
            
        #converting pdf to text
        convert(mytext,file)

        if os.path.getsize(file + ".mp3") == 0 or os.path.exists(file + ".mp3") == False:
            print("something went wrong!! Network error occured")
            print(f"failed to save {file}.mp3")
            print("You can try reconverting in a good network environment")
            print("Maybe you should try again")
            print(f"retrying...")

            start(0)

        print(f" DONE")
        print(f"filename: {file}.mp3")
        print(f"Want to convert more file ? ") 


        # get input to continue
        start(0)

        return(0)


# welcome display

print('welcome to pdf to speech')
print("Get started by identifiying the path to the pdf")
print("NOTE: copy and paste an existing pdf file name without '.pdf'.")
print("Y for yes.")  
print("N for no.")

# get input to start
print("starting...")

start(0)
