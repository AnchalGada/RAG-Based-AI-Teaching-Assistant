#converts videos to mp3
import os
import subprocess

files = os.listdir("videos")
for file in files:
    tutorial_number = file.split("#")[1].split(".")[0].split(" ")[0]
    file_name = file.split(" Sigma")[0].replace("(1)", "").strip()
    print(f"{tutorial_number}.{file_name}")
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}.{file_name}.mp3"])
