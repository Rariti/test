import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn('Для выполенние этой программы необъодима версия 3', RuntimeWarning)
else:
    print('Нормальное продолжение')