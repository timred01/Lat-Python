import sys

try:
    a = int(input("Masukkan sebuah bilangan positif: "))
    if a <= 0:
        raise ValueError("Itu bukan bilangan positif!")
except ValueError as ve: print(ve)