import os
import subprocess
import time

PATH = r"S:\Marketing\Commun\00. Documentation technique\1. DOC TECHNIQUE 2025"

folders = os.listdir(PATH)

QUALITY = ['ebook', 'screen', 'printer', 'prepress', 'default']


def compress_pdf(path_in: str, path_out: str, quality: str = "ebook"):
    executable = r"C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe"
    gs_command = [
        executable,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/" + quality,
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={path_out}",
        path_in,
    ]
    start_time = time.time()
    file_name = os.path.basename(path_in)
    print(f"Compressing {file_name}")

    try:
        subprocess.run(gs_command, check=True)
        print(f"Compressed {file_name} in {time.time() - start_time} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Error compressing {path_in}: {e}")


def main():
    for folder in folders:
        path_folder = os.path.join(PATH, folder)

        files = os.listdir(path_folder)
        for file in files:
            if file.endswith(".pdf"):
                path_pdf = os.path.join(path_folder, file)
                path_out = os.path.join(path_folder, file.replace(".pdf", "-compressed.pdf"))
                compress_pdf(path_pdf, path_out)


if __name__ == "__main__":
    main()
