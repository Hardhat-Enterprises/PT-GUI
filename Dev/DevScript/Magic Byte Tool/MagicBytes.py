import binascii
import PySimpleGUI as sg


mbytes = ["89 50 4E 47 0D 0A 1A 0A","FF D8 FF DB","FF D8 FF E0 00 10 4A 46 49 46 00 01", "FF D8 FF EE", "25 50 44 46 2d", "FF FB","EF BB BF","00 00 00 18 66 74 79 70","37 7A BC AF 27 1C","30 26 B2 75 8E 66 CF 11","42 4D","52 49 46 46","52 49 46 46","DB A5 2D 00","EC A5 C1 00","50 4B 03 04","D0 CF 11 E0 A1 B1 1A E1","47 49 46 38","FF D8 FF E0","FF D8 FF E1","	01 0F 00 00","4D 54 68 64","6D 6F 6F 76","49 44 33","00 00 01 B3","FD FF FF FF 43 00 00 00","38 42 50 53","52 61 72 21 1A 07 00","00 00 00 14 66 74 79 70","00 00 00 18 66 74 79 70","52 49 46 46","52 49 46 46","3C 21 64 6F 63 74 79 70","42 4D","DB A5 2D 00","50 4B 03 04","64 73 77 66 69 6C 65","44 56 44","58 2D","46 4C 56","1F 8B 08","4D 44 4D 50 93 A7","49 53 63 28","50 49 43 54 00 08","43 44 30 30 31","5F 27 A8 89","FF D8 FF E0","FF D8 FF E0","49 54 4F 4C 49 54 4C 53","50 4B 03 04","2A 2A 2A 20 20 49 6E 73","4D 41 72 30 00","01 0F 00 00","45 50","4D 54 68 64","1A 45 DF A3 93 42 82 88","6D 6F 6F 76","0C ED","00 00 01 B3","D0 CF 11 E0 A1 B1 1A E1","30 31 4F 52 44 4E 41 4E","D0 CF 11 E0 A1 B1 1A E1","38 42 50 53","E3 82 85 96","01 DA 01 01 00 03","4D 53 43 46","43 57 53","4D 5A","1F A0","49 20 49","FF 57 50 43","1D 7D","50 4B 03 04","3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D 22 31 2E 30 22 3F 3E","50 4B 03 04","50 4B 53 70 58","57 69 6E 5A 69 70"]
mtype = [".png",".jpg",".jpeg",".jpg", ".pdf", ".mp3",".UTF8",".MP4",".7Z",".WMD",".BMP",".CDR",".MPEG",".DOC",".DOC",".XML",".ODOC",".GIF","JFIF","EXIF",".SQL",".MIDI",".MOV",".MP3",".MPG",".PPT",".PSD","RAR",".3GP",".3GP5",".AVI",".DAT",".DCI",".DIB",".DOC",".DOCX",".DSW",".DVR",".EML",".FLV",".GZ",".HDMP",".HDR",".IMG",".ISO",".JAR",".JPE",".JPEG",".LIT",".KWD",".LOG",".MAR",".MDF",".MDI",".MIDI",".MKV",".MOV",".MP",".MPG",".MSI",".NTF",".PPT",".PSD",".PWL",".RGB",".SNP",".SWF",".SYS",".TAR.Z",".TIF",".WPD",".WS",".XLSX",".XML",".ZIP",".ZIP",".ZIP"]


def ReadFile():
    with open(filename, 'rb') as infile:
        while True:
            data = infile.read(1024)
            if not data:
                break
            return binascii.hexlify(data).decode('utf-8')
        


def PrintFileHex():
    filehex = ReadFile()
    return ' '.join(filehex[i:i+2] for i in range(0,len(filehex),2))


#Detect File Types
def DetectFileTypes():
    filehex = ReadFile()
    for mbyte in mbytes:
        if (mbyte.lower()).replace(" ", "") in filehex:
            print(mtype[mbytes.index(mbyte)])
            print(mbyte + "\n")


#add Hex to file
def ConvertMbytes():
    filehex = ReadFile()
    filepath = filename.split("/")
    basefile = filepath.pop(-1).split(".")[0]
    filepath="/".join(filepath)    
    f = open(filepath + "/New_" + basefile + values['-BYTES-'], 'w+b')
    sg.popup("File Saved at:",f)
    binary_format = bytearray.fromhex(mbytes[index])
    origionalFile = bytearray.fromhex(str(filehex))
    f.write(binary_format + origionalFile)


FileType = ''

sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                        'TEXT': '#E0E0E0',
                                        'INPUT': '#1C1C1E',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#32D74B',
                                        'BUTTON': ('#E0E0E0', '#32D74B'),
                                        'PROGRESS': ('#32D74B', '#333333'),
                                        'BORDER': 0,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0
                                    }
sg.theme('DarkMode') 

Column_1 =[[sg.Text('Choose the file',font ='Any 18',text_color='#E0E0E0')],
            [sg.Input(size=(30, 2)), sg.FileBrowse(font='Any 16')],
            [sg.Text('Select File Type',font ='Any 18',text_color='#E0E0E0'), sg.Combo(mtype, key='-BYTES-')],
            [sg.Button(' Convert ',font='Any 16'), sg.Text(' '*11), sg.Button(' Print Hex ',font='Any 16')] ]

Column_2 =[[sg.Button(' Detect Magic Bytes ',font='Any 16')],
           [sg.Output(size=(30, 5), key = '_output_')]]
                
       

            
layout = [[sg.Text('Welcome to Magic Byte Detector', font ='Any 28',text_color='#E0E0E0',key='-TEXT-')],
          [sg.Column(Column_1),
          sg.VSeparator(),
          sg.Column(Column_2)],
          [sg.ProgressBar(10, orientation='h', key='-PBAR-', size=(1240, 8))],
          [sg.Text(' '*60), sg.Button('Close',font='Any 16')]]

window = sg.Window('Magic Byte Tool', layout,size=(620,290),grab_anywhere=True)
while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])
    elif event == ' Convert ':
        if values['-BYTES-']:
            filename = values[0]
            index = mtype.index(values['-BYTES-'])
            hex_arr = mbytes[index]
            ConvertMbytes()
    
    elif event == ' Detect Magic Bytes ':
        window.FindElement('_output_').Update('')
        filename = values[0]
        DetectFileTypes()
        window.Refresh()
        
    elif event == ' Print Hex ':
        filename = values[0]
        sg.popup(PrintFileHex())
        
window.close()

