# ćwiczenie program liczący sumę wszystkich liczb do podanej liczby
import time

def sumuj_do(liczba_do):
    suma = 0
    for liczba in range(1,liczba_do+1):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba_do):
    return sum([liczba for liczba in range(1,liczba_do+1)])
    
def sumuj_do3(liczba_do):
    return int((1 + liczba_do) / 2 * liczba_do)

start = time.perf_counter()
print(sumuj_do(10000000))
print(finish_timer(start))
#print("czas sumuj_do", end-start)

start = time.perf_counter()
print(sumuj_do2(10000000))
end = time.perf_counter()
print("czas sumuj_do2", end-start)

start = time.perf_counter()
print(sumuj_do3(10000000))
end = time.perf_counter()
print("czas sumuj_do3 rerer", end-start)
