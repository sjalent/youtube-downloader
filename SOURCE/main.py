from pytube import YouTube
import uuid

asciiArt = "@@kkdd,,\'\'\'\',,,,,,\'\'....\'\'\'\'\'\',,,,,,,,,,,,\n@@kkkk,,,,,,,,....,,lloollddddll::,,,,,,,,\n@@kkkk;;\'\'..,,,,ooKKMMMMMMKKKKKKdd,,,,,,\'\'\nkkkkdd;;,,,,,,;;@@MMKKKKKKKKKKKK@@dd;;::,,\nkkkkdd::,,,,\'\'ooKKKKKKKKKKKK@@@@@@kk;;::,,\nkkddll::,,,,,,;;KKKKKK@@@@@@@@kkkkkkddll,,\nkkddoo;;;;;;ccKKKK@@@@kkkkkkddddddddddoo,,\nkkdd;;;;;;llKKKK@@@@ddddddlllllllldddddddd\nddll\'\',,::@@KK@@kkllccccoooooolllllllldd@@\nllcc..\'\'::@@@@kkoo::,,ccllooccllllllddKKMM\n::....\'\';;@@kkddoooolllllllloooollll@@MMMM\n\'\'\'\'\'\',,ccllcclllllllllloolllloollkkMMMMMM\n\'\'\'\'\'\',,oo;;::oooooooooooooooodd@@MMKKKKMM\n\'\'\'\'\'\';;cc::::::;;;;;;ccccooccKKMMKKKKMMMM\n\'\'\'\';;oocc;;::,,::::::::;;cccc@@KKKKMMMMKK\n,,ccoocccc;;,,\'\'cc;;::;;;;;;cckkKKKKMMKK@@\nccllcccc::::,,::llcc;;;;;;;;cckkKKMMKKKKKK\n::;;::::::,,oo@@kkllooccccccoo@@KKKKKKKK@@\n\'\'\'\'\'\',,,,ddKK@@kkddlllllloollkk@@@@@@@@@@\n......\'\'ooKK@@kkkkddddddddddddkk@@@@@@@@@@\n,,\'\'\'\',,kk@@kkkkddddddddddddkkkk@@@@@@@@@@"
print(asciiArt + "\n YOUTUBE DOWNLOADER IN PYTHON w\\o any bs")
print("            by szjalent\n\n")

def downloadFunc():
    print('###################################################################')
    titleOf = str(uuid.uuid1())

    videoToDownload = YouTube(input("Youtube link to download:\n"))
    directoryDownloadTo = input("\nWhere to save the video (leave blank if to root):\n")
    if directoryDownloadTo == "":
        print('\nDownloading to root...')
    else:
        print('\nDownloading to ' + directoryDownloadTo + "...")

    videoToDownload.streams.first().download(directoryDownloadTo, titleOf)
    if directoryDownloadTo == "":
        directoryDownloadTo = 'root directory'

    print('Done! Downloaded video to ' + directoryDownloadTo + ' as ' + titleOf + " .\n")

    print('###################################################################')

    isAll = input("Anything else? Y/N\n")
    if isAll == "y".upper():
        downloadFunc()
    else:
        input("Press any key to exit.")

downloadFunc()