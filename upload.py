import zipfile
import os

def main():
  walkedFiles = [file for file in os.walk("assets")]
  files = []
  for file in walkedFiles:
    concatinatedFile = file[0]
    for path in file[2]:
      concatinatedFile = concatinatedFile + "\\" + path
      files.append(concatinatedFile)
      concatinatedFile = file[0]
  
  zipFile = zipfile.ZipFile("pack.zip","w",zipfile.ZIP_DEFLATED)
  zipFile.write("pack.mcmeta")
  zipFile.write("pack.png")
  for file in files:
    zipFile.write(file)
  zipFile.close()

if __name__ == "__main__":
  main()
