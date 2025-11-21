import webview
from modules import encrypter, decrypter
class API:
    def encrypt_text(self, rawtext, a, b, c):
        try:
            return encrypter.encrypt_text(rawtext, a, b, c)
        except ValueError as e:
            raise e

    def decrypt_text(self, unprocessed_text_list, a, b, c):
        try:
            return decrypter.decrypt_text(unprocessed_text_list, a, b, c)
        except ValueError as e:
            raise e
if __name__ == "__main__":
    api = API()
    window = webview.create_window(
        "Cryptography Algorithm",
        "web/index.html",
        js_api=api
    )
    webview.start(debug=True)