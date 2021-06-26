import pyqrcode

url = pyqrcode.create('put something to generate qrcode')

#save the file #for png mode install pypng using pip command 
url.svg('uca-url.svg', scale=8)

url.eps('uca-url.eps', scale=2)
# to show in terminal 
print(url.terminal(quiet_zone=1))