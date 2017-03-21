import os
for i in range(1, 54):
    url = "https://ftp.mozilla.org/pub/firefox/releases/" + str(i) + ".0/win32/en-US/Firefox Setup " + str(i) + ".0.exe"
    os.system("wget '" + url + "'")
    print url

