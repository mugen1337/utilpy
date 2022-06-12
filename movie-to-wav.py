import glob
import subprocess
import os

in_dir  = "/hoge/"
out_dir = "/fuga/"

def main():
    files = []
    files += glob.glob(in_dir + "*.mov")
    files += glob.glob(in_dir + "*.webm")
    files += glob.glob(in_dir + "*.mp4")

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    

    for file in files:
        name = os.path.splitext(os.path.basename(file))[0]
        out_path = out_dir + name + ".wav"

        if not os.path.exists(out_path):
            subprocess.run(["ffmpeg", "-i", file, "-ac", "1", "-f", "wav", out_path])

if __name__ == "__main__":
    main()
