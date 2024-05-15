def my_mp3_playlist(file_path):
    array = ['', '0', '']
    with open(file_path, 'r') as file:
        songs = file.readlines()
        for song in songs:
            parts = song.strip().split(';')
            if len(parts[0]) > len(array[0]):
                array[0] = parts[0]
            if len(parts[2]) > len(array[2]):
                array[2] = parts[2]
            if int(array[1]) < int(parts[1].split(':')[0]):
                array[1] = parts[1].split(':')[0]
    return tuple(array)

print(my_mp3_playlist("hangman-unit9/songs.txt"))




