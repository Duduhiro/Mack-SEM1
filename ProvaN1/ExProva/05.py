sec = int(input("Sec: "))

if sec >= 60 :
    min = sec // 60
    sec = sec % 60
if min >= 60 :
    hour = min // 60
    min = min % 60
print(f"Horário {hour}:{min}:{sec}")