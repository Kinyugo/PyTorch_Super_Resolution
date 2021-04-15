import os

import requests


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    os.makedirs("./checkpoints", exist_ok=True)

    # Download checkpoints from google drive
    # https://drive.google.com/file/d/16MygTm9Ba1rmQfldOyGU8zY-Ike6E9qa/view?usp=sharing
    ssrresnet_id = "16MygTm9Ba1rmQfldOyGU8zY-Ike6E9qa"
    ssrresnet_dest = "./checkpoints/checkpoint_srresnet.pth.tar"

    # https://drive.google.com/file/d/1--FmF5_fR8v9h8dngJ44DtcowpMX4vPp/view?usp=sharing
    ssrgan_id = "1--FmF5_fR8v9h8dngJ44DtcowpMX4vPp"
    ssrgan_dest = "./checkpoints/checkpoint_srgan.pth.tar"

    download_file_from_google_drive(ssrresnet_id, ssrresnet_dest)
    # download_file_from_google_drive(ssrgan_id, ssrgan_dest)
