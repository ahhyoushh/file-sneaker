from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilenames()

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
         
drive = GoogleDrive(gauth)


upload_file_list = [file_path]

for upload_file in upload_file_list:
    if sys.argv[1] == "--root":
        gfile = drive.CreateFile({'parents': [{'id': '1lPPfyqRfls-Gpty_gMK7svniLmFEZwy8'}]})
    else:
        gfile = drive.CreateFile({'parents': [{'id': '1R8FL_8S0gXWI7w7wG0dYiMGJnZdomzfx'}]})
    
    gfile.SetContentFile(upload_file)
    gfile.Upload()

print("Succesfull!")