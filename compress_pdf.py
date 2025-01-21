import os
import subprocess
import time

PATH = r"S:\Marketing\Commun\00. Documentation technique\4. Modifications à valider\FILTRY"


class Quality:
    def __init__(self):
        self.ebook = "ebook"
        self.screen = "screen"
        self.printer = "printer"
        self.prepress = "prepress"
        self.default = "default"


def compress_pdf(path_in: str, path_out: str, quality: str = Quality().ebook):
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
        print(f"Compressed {file_name} in {round(time.time() - start_time, 2)} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Error compressing {path_in}: {e}")


def main():
    paths = set(os.listdir(PATH))

    while paths:
        path = paths.pop()
        print("Traitement de : " + path)

        if path.endswith(".pdf") and not path.endswith("-compressed.pdf"):
            print("C'est un fichier PDF compression en cours !")
            path_in = os.path.join(PATH, path)
            path_out = os.path.join(PATH, path.replace(".pdf", "-compressed.pdf"))
            compress_pdf(path_in, path_out)
        elif len(path.split(".")) == 1:
            print("Cest un dossier")
            paths.add(path)


if __name__ == "__main__":
    main()
