## Поиск места встречи

Этот репозиторий содержит пет-проект, предназначенный для поиска оптимальной станции метро для встречи группы людей.

## Описание

Программа позволяет определить наиболее удобную станцию метро, основываясь на местоположении участников. Вам нужно указать список станций метро, где живут люди, и программа вычислит оптимальную по времени достижения каждым участником станцию для встречи.

## Установка
   ```bash
   git clone https://github.com/EugeneGorbulya/MeetPointMetro/
   cd MeetPointMetro
   ```
## Использование

1. Откройте файл `parameters.csv` и добавьте список станций метро, где живут участники. Формат файла:
   ```
   Station
   станция1
   станция2
   станция3
   ```
2. Запустите программу:
   ```bash
    python3 main.py
   ```
3. В результате выполнения программы вы получите оптимальную станцию метро для встречи.
   
