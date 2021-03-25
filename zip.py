from zipfile import ZipFile
import os
# // just put the name and location file
os.chdir(r'location file')
ZipFile('archive.zip', 'w').write('your file name with type')