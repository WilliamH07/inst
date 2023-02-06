import requests
import time
from ftplib import FTP
ftp = FTP('FTP.thecorrector.x10.mx', 'william@thecorrector.x10.mx', 'William*200019')  

start_time = time.time()

# INSTAGRAM

# Enter File Name with Extension
filename = "data.txt"
    
    # Write file in binary mode
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp.retrbinary(f"RETR {filename}", file.write)
    
    
# Display the content of downloaded file
file=open(filename, "r")


# Close the Connection
ftp.quit()

# APPLE

ftp = FTP('FTP.thecorrector.x10.mx', 'data@thecorrector.x10.mx', 'William*200019') 

# Enter File Name with Extension
filename = "credentials.txt"
    
# Write file in binary mode
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp.retrbinary(f"RETR {filename}", file.write)
    
# Display the content of downloaded file
file= open(filename, "r")

# Close the Connection
ftp.quit()



