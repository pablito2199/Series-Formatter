from pathlib import Path

path = input("Enter the path to the series' files: ")
serie = input("Enter the series' name: ")
season = input(f"Enter the season from {serie}: ")
extension = input("Enter the file extension (e.g: mp4): ")
chapter = 1

for file in Path(path).iterdir():
    if file.is_file():
        new_name = serie + " S" + season.zfill(2) + "E" + str(chapter).zfill(2) + "." + extension
        file.rename(Path(path, new_name))
        print(file.stem + " --> " + new_name)
        chapter += 1
