# esse projeto tem objetivo criar uma ferramenta pessoal de uso próprio
import qrcode
from PIL import Image

class createQrCode():
    
    @staticmethod
    def form():
        link = input('insira o link do seu qrcode aqui: \n')
        name = input('insira aqui que nome você quer dar a seu QrCode: \n')
        return link, name
    

    def criarQrcode(link, name):
        img = qrcode.make(link)

        img.save(f'{name}.png')

if __name__ == "__main__":
    
    link_do_qrcode, nome_do_arquivo = createQrCode.form()
    createQrCode.criarQrcode(link_do_qrcode, nome_do_arquivo)
    print(f"QR Code '{nome_do_arquivo}.png' criado com sucesso!")
