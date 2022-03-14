# Hash Analyzer
# By Willem Tranku

import base64
import re
import os

# Version
version = 1.0

# Banner
logo =  """=====================
           Hash Analyzer
                  v{v}
=====================""".format(v = version)

# Encoding algorithms
encoding_algorithms = {
    "100000":"Base16", "100001":"Base32", "100002":"Base64"
}

# Hash algorithms (includes Checksums)
algorithms = {
    "100400":"CRC-16(Checksum)",
    "100800":"Adler-32(Checksum)", "100801":"CRC-32(Checksum)",
    "101300":"DES(Unix)",
    "103200":"MD5", "103201":"Tiger-128", "103202":"NTLM", "103203":"Haval-128", "103204":"MD4", "103205":"MD2",
    "104000":"SHA-1", "104001":"RipeMD-160", "104002":"Tiger-160", "104003":"Haval-160",
    "104800":"Tiger-192", "104801":"Haval-192",
    "105600":"SHA-224", "105601":"SHA3-224", "105602":"Haval-224",
    "106400":"SHA-256", "106401":"SHA3-256", "106402":"RipeMD-256", "106403":"Haval-256",
    "108000":"RipeMD-320",
    "109600":"SHA-384", "109601":"SHA3-384",
    "112800":"SHA-512", "112801":"Whirlpool", "112802":"SHA3-512"
    }

# List of hash algorithms
def md5(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103200")

def md4(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103204")

def md2(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103205")

def sha1(hash):
    if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
        hashes.append("104000")

def sha224(hash):
    if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
        hashes.append("105600")

def sha3224(hash):
    if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
        hashes.append("105601")

def sha256(hash):
    if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
        hashes.append("106400")

def sha3256(hash):
    if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
        hashes.append("106401")

def sha384(hash):
    if (re.search(r'([a-fA-F0-9]{96})', hash) != None and len(hash) == 96):
        hashes.append("109600")

def sha3384(hash):
    if (re.search(r'([a-fA-F0-9]{96})', hash) != None and len(hash) == 96):
        hashes.append("109601")

def sha512(hash):
    if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
        hashes.append("112800")

def sha3512(hash):
    if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
        hashes.append("112802")

def ripemd160(hash):
    if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
        hashes.append("104001")

def ripemd256(hash):
    if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
        hashes.append("106402")

def ripemd320(hash):
    if (re.search(r'([a-fA-F0-9]{80})', hash) != None and len(hash) == 80):
        hashes.append("108000")

def tiger128(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103201")

def tiger160(hash):
    if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
        hashes.append("104002")

def tiger192(hash):
    if (re.search(r'([a-fA-F0-9]{48})', hash) != None and len(hash) == 48):
        hashes.append("104800")
    
def whirlpool(hash):
    if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
        hashes.append("112801")

# Check for base16
def base16check(hash):
    try:
        #Decode the string and encode it back to base16 to check if it is a real base16 string and is convertible to UTF-8
        if (base64.b16encode(base64.b16decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100000"] = base64.b16decode(hash).decode('utf-8') # If it is decode its results and show it
            encodings.append("100000")
    except base64.binascii.Error: # If it is not a base16, no need to do anything
        pass
    except UnicodeDecodeError: # If it is not convertible to a UTF-8 string, no need to do anything
        pass

# Check for base32
def base32check(hash):
    try:
        #Decode the string and encode it back to base32 to check if it is a real base32 string and is convertible to UTF-8
        if (base64.b32encode(base64.b32decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100001"] = base64.b32decode(hash).decode('utf-8') # If it is decode its results and show it
            encodings.append("100001")
    except base64.binascii.Error: # If it is not a base16, no need to do anything
        pass
    except UnicodeDecodeError: # If it is not convertible to a UTF-8 string, no need to do anything
        pass

# Check for base64
def base64check(hash):
    try:
        #Decode the string and encode it back to base64 to check if it is a real base64 string and is convertible to UTF-8
        if (base64.b64encode(base64.b64decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100002"] = base64.b64decode(hash).decode('utf-8') # If it is decode its results and show it
            encodings.append("100002")
    except base64.binascii.Error: # If it is not a base16, no need to do anything
        pass
    except UnicodeDecodeError: # If it is not convertible to a UTF-8 string, no need to do anything
        pass

def adler32(hash):
    if (re.search(r'([a-fA-F0-9]{8})', hash) != None and len(hash) == 8):
        hashes.append("100800")

def ntlm(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103202")

def crc16(hash):
    if (re.search(r'([a-fA-F0-9]{4})', hash) != None and len(hash) == 4):
        hashes.append("100400")

def crc32(hash):
    if (re.search(r'([a-fA-F0-9]{8})', hash) != None and len(hash) == 8):
        hashes.append("100801")

def desunix(hash):
    if (re.search(r'([./0-9A-Za-z]{13})', hash) != None and len(hash) == 13):
        hashes.append("101300")

def haval128(hash):
    if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
        hashes.append("103203")

def haval160(hash):
    if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
        hashes.append("104003")

def haval192(hash):
    if (re.search(r'([a-fA-F0-9]{48})', hash) != None and len(hash) == 48):
        hashes.append("104801")

def haval224(hash):
    if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
        hashes.append("105602")

def haval256(hash):
    if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
        hashes.append("106403")

# Read hashes from a file
def read_file(filename):
    output = filename + ':\n' # Store all the outputs in this string to be returned
    try:
        f = open(filename, "r") # Open the file in read mode
        for line in f: # Loop each line in the file
            line = line.strip() # Strip the newline characters
            hash_check(line) # Perform the hash checkers to each hash
            if (len(hashes) > 0): # If there is at least 1 possible hash found, add them to the output string
                hashes.sort()
                output += line + ": Possible algorithms ("
                for s in hashes:
                    output += algorithms[s] + ", "
                output = output[:len(output)-2] + ')'
            if (len(encodings) > 0): # If there is at least 1 possible encoding found, add them to the output string
                output += "; Possible encodings ("
                for e in encodings:
                    output += encoding_algorithms[e] + ", "
                output = output[:len(output)-2] + ')'
            if (len(hashes) == 0 and len(encodings) == 0): # If there is no results, do not add a newline nor clear the lists
                continue

            output += "\n" # Add a newline to each results

            del hashes[:] # Clear the possible hashes list
            del encodings[:] # Clear the possible encodings list
        f.close() # Close the file if everything is completed.
    except FileNotFoundError: # If file name is not found, add a "File not found." to the output string
        output += "File not found."
    except: # If an unknown error appears after the file is opened, close the file and print a generic error message and raise the error
        f.close()
        output += "An error has occured..."
        raise
    finally: # Returns the output regardless of if there is an error or not
        return output

def single_hash(hash):
    output = hash + ':\n' # Store all the outputs in this string to be returned
    try:
        hash_check(hash) # Perform the hash checkers to the hash
        if len(hashes) == 0: # If there is at least 1 possible hash found, add them to the output string
            output += "Possible hashes not found."
        else:
            hashes.sort()
            output += "Possible hashes:"
            for s in hashes:
                output += "\n[+] " + algorithms[s]
        if len(encodings) > 0: # If there is at least 1 possible encoding found, add them to the output string
            output += "\nPossible encodings:\n"
            for e in encodings:
                output += "[+] " + encoding_algorithms[e] + " -> " + decode_results[e] + "\n"
    except: # If an unknown error appears, print a generic error message and raise the error
        output += "An error has occured..."
        raise
    finally: # Returns the output regardless of if there is an error or not
        return output

def hash_check(h):
    try:
        # Hash algorithms
        md5(h); md4(h); md2(h)
        sha1(h); sha224(h); sha3224(h); sha256(h); sha3256(h); sha384(h); sha3384(h); sha512(h); sha3512(h)
        haval128(h); haval160(h); haval192(h); haval224(h); haval256(h)
        ripemd160(h); ripemd256(h); ripemd320(h)
        tiger128(h); tiger160(h); tiger192(h)
        whirlpool(h); ntlm(h); desunix(h)
        adler32(h); crc16(h); crc32(h)

        # Encodings
        base16check(h); base32check(h); base64check(h)
    except: # Raise any errors found
        raise

def hash_analyze(inp, type):
    if (len(inp.strip()) != 0): # If input is not blank
        output = ""
        try:
            global hashes
            global encodings
            global decode_results
            
            hashes = [] # List to save the possible hashes
            encodings = [] # List to save the possible encodings
            decode_results = {} # List to save the encoding results

            if (type == "Hash"): # If 1, get user input for a hash then check and print the output string
                output += single_hash(inp)
            elif (type == "File"): # If 2, get user input for a file name then check and print the output string
                output += read_file(inp)

        except: # If any other errors encountered, raise the error 
            raise
        finally:
            output += '\n'
            return output
    return "No input found.\n"

# ====================
# GUI code starts here
# ====================

import PySimpleGUI as sg

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
sg.SetOptions(element_padding=(8,8))

def MAKE_Hash_Analyzer():

    HASH = "Hash     : "
    FILE = "Filename: "

    layout = [  [sg.Text(HASH, font='Any 26', text_color='#E0E0E0', key='-IN1 TEXT-'),
                    sg.InputText(font='Any 24', text_color='#E0E0E0', key='-IN1-', focus=True),
                    sg.pin(sg.Column([ [ sg.FileBrowse(font='Any26', target='-IN1-') ] ], key='-BROWSE-', visible=False)),
                    sg.Combo(["Hash","File"], default_value='Hash', font='Any 24', enable_events=True, key="-COMBO-", readonly=True)],

                [sg.Button('Analyze', font='Any 24', key="-ANALYZE-", bind_return_key=True),
                    sg.Button('Close', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
                [sg.Multiline(logo + '\n\n', disabled=True, write_only=True, autoscroll=True, size=(1240, 30), text_color='#E0E0E0', font='Any 12', key="-OUTPUT-"+sg.WRITE_ONLY_KEY)] ]

    return sg.Window('Hash Analyzer', layout, size=(1280,720), finalize=True)

def CHECK_Hash_Analyzer(window, event, values):
    HASH = "Hash     : "
    FILE = "Filename: "

    if event == sg.WIN_CLOSED or event == 'Close':
        window.close()

    elif event.startswith('-COMBO-'):
        combo = values['-COMBO-']
        if combo == 'Hash':
            window['-IN1 TEXT-'].update(HASH)
            window['-BROWSE-'].update(visible=False)
        else:
            window['-IN1 TEXT-'].update(FILE)
            window['-BROWSE-'].update(visible=True)

    elif event.startswith('-ANALYZE-'):
        inp = values['-IN1-']
        combo = values['-COMBO-']
        window['-OUTPUT-'+sg.WRITE_ONLY_KEY].print(hash_analyze(inp, combo))

#if __name__ == '__main__':
#    Hash_Analyzer()