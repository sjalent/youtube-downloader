from pytube import YouTube
import uuid

asciiArt = '@@kkdd,,\'\'\'\',,,,,,\'\'....\'\'\'\'\'\',,,,,,,,,,,,\n@@kkkk,,,,,,,,....,,lloollddddll::,,,,,,,,\n@@kkkk;;\'\'..,,,,ooKKMMMMMMKKKKKKdd,,,,,,\'\'\nkkkkdd;;,,,,,,;;@@MMKKKKKKKKKKKK@@dd;;::,,\nkkkkdd::,,,,\'\'ooKKKKKKKKKKKK@@@@@@kk;;::,,\nkkddll::,,,,,,;;KKKKKK@@@@@@@@kkkkkkddll,,\nkkddoo;;;;;;ccKKKK@@@@kkkkkkddddddddddoo,,\nkkdd;;;;;;llKKKK@@@@ddddddlllllllldddddddd\nddll\'\',,::@@KK@@kkllccccoooooolllllllldd@@\nllcc..\'\'::@@@@kkoo::,,ccllooccllllllddKKMM\n::....\'\';;@@kkddoooolllllllloooollll@@MMMM\n\'\'\'\'\'\',,ccllcclllllllllloolllloollkkMMMMMM\n\'\'\'\'\'\',,oo;;::oooooooooooooooodd@@MMKKKKMM\n\'\'\'\'\'\';;cc::::::;;;;;;ccccooccKKMMKKKKMMMM\n\'\'\'\';;oocc;;::,,::::::::;;cccc@@KKKKMMMMKK\n,,ccoocccc;;,,\'\'cc;;::;;;;;;cckkKKKKMMKK@@\nccllcccc::::,,::llcc;;;;;;;;cckkKKMMKKKKKK\n::;;::::::,,oo@@kkllooccccccoo@@KKKKKKKK@@\n\'\'\'\'\'\',,,,ddKK@@kkddlllllloollkk@@@@@@@@@@\n......\'\'ooKK@@kkkkddddddddddddkk@@@@@@@@@@\n,,\'\'\'\',,kk@@kkkkddddddddddddkkkk@@@@@@@@@@'
print(asciiArt + '\nYOUTUBE DOWNLOADER IN PYTHON')
print('by szjalent\n')

def downloadOptions(video):

    print('\nChecking for downloadable streams...')


    stream1080P = [video.streams.get_by_itag(299), '1080p']
    stream720P = [video.streams.get_by_itag(22), '720p']
    stream480P = [video.streams.get_by_itag(135), '480p']
    stream360P = [video.streams.get_by_itag(18), '360p']
    stream240P = [video.streams.get_by_itag(133), '240p']
    stream144P = [video.streams.get_by_itag(160), '144p']
    streamAUDIO = [video.streams.get_by_itag(140), 'audio']

    streamArray = [stream1080P, stream720P, stream480P, stream360P, stream240P, stream144P, streamAUDIO]

    if len(streamArray[0]) and len(streamArray[1]) and len(streamArray[2]) and len(streamArray[3]) and len(streamArray[4]) and len(streamArray[5]) and len(streamArray[6]) == 1:
        print('The video you\'re trying to download (somehow) has no downloadable streams available.')
        input('Press any key to exit.')
        exit()

    print('\nChoose downloadable stream:\n\n1) 1080p video\n2) 720p video\n3) 480p video\n4) 360p video\n5) 240p video\n6) 144p video\n7) audio only')

    def chooseDnldStream(stream):
        streamInput = input('\n>> ')
        x = 0
        if streamInput.isnumeric():
            x = int(streamInput)
        else:
            print('Input a valid number')
            chooseDnldStream(streamArray)
        chosenStream = stream[(x - 1) % 7]
        vidayo = chosenStream[0]
        if type(vidayo) is not type('text') and vidayo != None:
            return vidayo
        else:
            print('Couldn\'t find desired stream, please choose another.')
            chooseDnldStream(streamArray)

    return chooseDnldStream(streamArray)


def downloadFunc():
    print('\n###################################################################\n\nYoutube link to download:')

    while True:
        eenput = input('>> ')
## regex is too much man
        if 'https://www.youtube.com' in eenput or 'https://youtu.be' in eenput:
            videoStreams = YouTube(eenput)
            break
        else:
            print('Provide a valid Youtube URL\n')

    videoToDownload = downloadOptions(videoStreams)

    titleOf = videoToDownload.title + ' - ' + str(uuid.uuid1())[0:7]
    directoryDownloadTo = input('\nWhere to save the video (leave blank if to root):\n>> ')
    print('Proccessing...\n')
    if directoryDownloadTo == '':
        print('Downloading to root... (' + str(int(videoToDownload.filesize) / 1000000) + 'MB)')
    else:
        print('Downloading to ' + directoryDownloadTo + '...')

    videoToDownload.download(directoryDownloadTo, titleOf)

    print('\nDone! Downloaded video to ' + directoryDownloadTo + ' as ' + titleOf + ' .\n')

    print('\n###################################################################')

    isAll = input('\nAnything else? Y/N\n>> ')
    if isAll == 'y'.upper():
        downloadFunc()
    else:
        input('Press any key to exit.')

downloadFunc()