import zipfile
with zipfile.ZipFile("file.zip","r") as zip_ref:
    dat_file = zip_ref.namelist()
    dat_filename = dat_file[0]
    print dat_filename
    zip_ref.extractall("")
