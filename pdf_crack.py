import pikepdf as pdfc
from tqdm import tqdm

filename = "abc.pdf"
wordlist = "wordlist.txt"

# load passwords list or dictionary.
password = [line.strip() for line in open(wordlist)]
# working on password.
for password in tqdm(password, "Decrypting PDF"):
    try:
        with pdfc.open(filename, password=password) as pdf:
            print("[+] Password Found : ", password)
            break
    except pdfc._qpdf.PasswordError as e:
        continue
