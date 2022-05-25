# Desafio 3

3) Devido aos efeitos da globalização e visando o lucro, uma rede de caixas de supermercado resolver adotar diversas moedas diferentes, tais como dolar e euro, pensando nisso desenvolva um programa que calcule automáticamente a conversão da moeda.

```python
real_para_euro = 6.5
real_para_dolar = 5.0

real = float(input('Digite o valor em reais'))
print(f'{real} reais é equivalente a {real*real_para_dolar} dólares e {real*real_para_euro}')
print()
```