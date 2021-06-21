from pytube import YouTube
import uuid

asciiArt = '@@kkdd,,\'\'\'\',,,,,,\'\'....\'\'\'\'\'\',,,,,,,,,,,,\n@@kkkk,,,,,,,,....,,lloollddddll::,,,,,,,,\n@@kkkk;;\'\'..,,,,ooKKMMMMMMKKKKKKdd,,,,,,\'\'\nkkkkdd;;,,,,,,;;@@MMKKKKKKKKKKKK@@dd;;::,,\nkkkkdd::,,,,\'\'ooKKKKKKKKKKKK@@@@@@kk;;::,,\nkkddll::,,,,,,;;KKKKKK@@@@@@@@kkkkkkddll,,\nkkddoo;;;;;;ccKKKK@@@@kkkkkkddddddddddoo,,\nkkdd;;;;;;llKKKK@@@@ddddddlllllllldddddddd\nddll\'\',,::@@KK@@kkllccccoooooolllllllldd@@\nllcc..\'\'::@@@@kkoo::,,ccllooccllllllddKKMM\n::....\'\';;@@kkddoooolllllllloooollll@@MMMM\n\'\'\'\'\'\',,ccllcclllllllllloolllloollkkMMMMMM\n\'\'\'\'\'\',,oo;;::oooooooooooooooodd@@MMKKKKMM\n\'\'\'\'\'\';;cc::::::;;;;;;ccccooccKKMMKKKKMMMM\n\'\'\'\';;oocc;;::,,::::::::;;cccc@@KKKKMMMMKK\n,,ccoocccc;;,,\'\'cc;;::;;;;;;cckkKKKKMMKK@@\nccllcccc::::,,::llcc;;;;;;;;cckkKKMMKKKKKK\n::;;::::::,,oo@@kkllooccccccoo@@KKKKKKKK@@\n\'\'\'\'\'\',,,,ddKK@@kkddlllllloollkk@@@@@@@@@@\n......\'\'ooKK@@kkkkddddddddddddkk@@@@@@@@@@\n,,\'\'\'\',,kk@@kkkkddddddddddddkkkk@@@@@@@@@@'
print(asciiArt + '\nYOUTUBE DOWNLOADER IN PYTHON')
print('by szjalent\n')

def downloadFunc():
    print('\n###################################################################')

    videoToDownload = YouTube(input('Youtube link to download:\n>> '))
    titleOf = videoToDownload.title + ' - ' + str(uuid.uuid1())[0:7]
    directoryDownloadTo = input('\nWhere to save the video (leave blank if to root):\n>> ')
    if directoryDownloadTo == '':
        print('\nDownloading to root...')
    else:
        print('\nDownloading to ' + directoryDownloadTo + '...')

    videoToDownload.streams.first().download(directoryDownloadTo, titleOf)

    print('\nDone! Downloaded video to ' + directoryDownloadTo + ' as ' + titleOf + ' .\n')

    print('\n###################################################################')

    isAll = input('\nAnything else? Y/N\n>> ')
    if isAll == 'y'.upper():
        downloadFunc()
    else:
        input('Press any key to exit.')

downloadFunc()