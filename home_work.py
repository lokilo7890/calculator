# class  Airplane:
#     engines = input("ведите число двигатилей\n")
#     seats = input("ведите число мест\n")
# ariplane = Airplane()
# print(ariplane.engines)
# print(ariplane.seats)


import qrcode

data = 'https://cloud.mail.ru/public/cBzA/KxmiuV6gp'

qr = qrcode.QRCode(version=5, box_size=15, border=10)

qr.add_data(data)

img = qr.make_image()

img.save('test.png')

# функция eval() принитмает тескт и выполняет его как код пайтон