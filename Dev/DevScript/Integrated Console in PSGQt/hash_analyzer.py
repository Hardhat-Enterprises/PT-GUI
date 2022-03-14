# Hash Analyzer
# By Willem Tranku

from sys import exit
import base64
import re
import os

version = 1.0

logo =  """=====================
    Hash Analyzer
        v{v}
=====================""".format(v = version)

encoding_algorithms = {
    "100000":"Base16", "100001":"Base32", "100002":"Base64"
}

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

def base16check(hash):
    try:
        if (base64.b16encode(base64.b16decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100000"] = base64.b16decode(hash).decode('utf-8')
            encodings.append("100000")
    except base64.binascii.Error:
        pass
    except UnicodeDecodeError:
        pass

def base32check(hash):
    try:
        if (base64.b32encode(base64.b32decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100001"] = base64.b32decode(hash).decode('utf-8')
            encodings.append("100001")
    except base64.binascii.Error:
        pass
    except UnicodeDecodeError:
        pass

def base64check(hash):
    try:
        if (base64.b64encode(base64.b64decode(hash)).decode('utf-8') == hash and hash != ""):
            decode_results["100002"] = base64.b64decode(hash).decode('utf-8')
            encodings.append("100002")
    except base64.binascii.Error:
        pass
    except UnicodeDecodeError:
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


def ReadFile(filename):
    try:
        f = open(os.path.abspath(os.path.dirname(__file__)) + "/" + filename, "r")
        output = ""
        for line in f:
            line = line.replace("\n", "")
            HashCheck(line)
            if (len(hashes) > 0):
                hashes.sort()
                output += line + ": Possible algorithms ("
                for s in hashes:
                    output += algorithms[s] + ", "
                output = output[:len(output)-2] + ')'
            if (len(encodings) > 0):
                output += "; Possible encodings ("
                for e in encodings:
                    output += encoding_algorithms[e] + ", "
                output = output[:len(output)-2] + ')'
            output += "\n"

            del hashes[:]
            del encodings[:]

    except Exception as ex:
        print(ex)
        output += "\nAn error has occured..."
    finally:
        f.close()
        return output

def HashCheck(h):
    try:
        # Hashes
        md5(h); md4(h); md2(h)
        sha1(h); sha224(h); sha3224(h); sha256(h); sha3256(h); sha384(h); sha3384(h); sha512(h); sha3512(h)
        haval128(h); haval160(h); haval192(h); haval224(h); haval256(h)
        ripemd160(h); ripemd256(h); ripemd320(h)
        tiger128(h); tiger160(h); tiger192(h)
        whirlpool(h); ntlm(h); desunix(h)
        adler32(h); crc16(h); crc32(h)

        # Encodings
        base16check(h); base32check(h); base64check(h)
    except:
        raise

if __name__ == "__main__":
    print(logo)
    while True:
        try:
            hashes = []
            encodings = []
            decode_results = {}
            
            print("-"*50)

            #filename = input("Please enter a file name:\n")
            #print(ReadFile(filename))
            
            h = input("Please enter a hash value:\n")
            HashCheck(h)

            if len(hashes) == 0:
                print("\nPossible hashes not found.")
            else:
                hashes.sort()
                print("\nPossible hashes:")
                for s in hashes:
                    print("[+] " + algorithms[s])
            if len(encodings) > 0:
                print("\nPossible encodings:")
                for e in encodings:
                    print("[+] " + encoding_algorithms[e] + " -> " + decode_results[e])

        except:
            print("\n\nThanks for using Hash Analyzer.")
            raise