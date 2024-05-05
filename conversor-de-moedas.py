real = float(input('Quanto você tem na sua carteira?R$'))
dolar = real / 5.07
euro = real / 5.49
libra = real / 6.40
iene = real /0.033
print('Com R${} você pode comprar US${}' .format(real, dolar))
print('Com R${} você pode comprar €{}' .format(real, euro))
print('Com R${} você pode comprar £{}' .format(real, libra))
print('Com R${} você pode comprar ¥{}' .format(real, iene))


