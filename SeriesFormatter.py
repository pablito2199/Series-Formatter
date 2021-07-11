from pathlib import Path

path = input("Which is the path to the series' files? ")
serie = input("Which is the series' name? ")
season = input("Which is the season from {serie}? ")
extension = input("Which is your file extension? (e.g: mp4) ")
chapter = 1

for file in Path(path).iterdir():
    if file.is_file():
        new_name = serie + " S" + season.zfill(2) + "E" + str(chapter).zfill(2) + "." + extension
        file.rename(Path(path, new_name))
        chapter += 1