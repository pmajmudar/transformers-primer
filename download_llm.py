import os
import urllib.request


def download_file(file_link, filename):
    print("Starting download of {}".format(file_link))

    # Checks if the file already exists before downloading
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(file_link, filename)
        print("File downloaded successfully.")
    else:
        print("File already exists.")



if __name__ == "__main__":
    # Dowloading GGML model from HuggingFace
    ggml_model_path = "https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/resolve/main/zephyr-7b-beta.Q4_0.gguf"
    filename = os.path.split(ggml_model_path)[-1]
    
    download_file(ggml_model_path, filename)
