import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.

sours = ['C:\\Users\Admin\Desktop\papka1', 'C:\\Users\Admin\Desktop\papka2']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва
target_dir = 'C:\\Users\Admin\Desktop\gde_hranim' #Здесь мы подставляем свой путь
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.

today = target_dir + os.sep + time.strftime('%Y%m%d')
print('Так выглядит today', today)
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
print('Так выглядит now', now)

if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print("Каталог успешно создан", today)
else:
    print('Каталог уже есть')

# Имя zip-файла
target = today + os.sep + now + '.zip'
print('Так выглядит target', target)
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(sours))
print('Так выглядит zip_command', zip_command)

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Команда выполнена успешно', target)
else:
    print('Команда НЕ ВЫПОЛНЕНА')