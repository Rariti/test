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
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(sours))
# Запускаем создание резервной копии

print('zip_command: ', zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
