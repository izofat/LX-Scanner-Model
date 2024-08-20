import argparse

from lx_scanner_model.ai_model.pretrained import OpticalCharacterRecognition


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p", "--path", type=str, required=True, help="Path to the file"
    )
    parser.add_argument(
        "-l", "--lang", type=str, required=True, help="Language you wanna use"
    )

    args = parser.parse_args()

    ocr_model = OpticalCharacterRecognition(args.path, args.lang)
    print(ocr_model.output.text)
    ocr_model.image_helper.display_image()
