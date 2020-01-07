"""
"""


# -- num 111--------------------------------
def div3(num1, num2):
    return 0 if num2 == 0 else num1 / num2


ans = input('Введите 2 числа для деления, разделенных пробелом : ').split()
print(div3(float(ans[0]), float(ans[1])))


# -- num 222--------------------------------


def userdata(name='', surname='', tel='', location='', yearborn=''):
    print(f'{name.title()} {surname.title()}. Год рождения : {yearborn}.  {location.title()} тел: {tel} ')


userdata('fedor', 'seLIN', location='ivanovo', tel='+7899889', yearborn='1990')
userdata(tel='+397899889', location='MSK', name='Victor', surname='LenIN', yearborn=1997)


# -- num 333 --------------------------------

def ro_summ(poz1, poz2, poz3):
    try:
        x = float(poz1)
    except ValueError:
        x = 0
    try:
        y = float(poz2)
    except ValueError:
        y = 0
    try:
        z = float(poz3)
    except ValueError:
        z = 0

    lis = sorted([x, y, z])
    print('Переданы значения ', lis, 'Sum = ', lis[1] + lis[2])


ro_summ(12, 14, 12.3)
ro_summ('erw', '23', '23.445')


# -------- 4 -----------------------------------
def ro_milti(num1, step):
    st = 1
    nums = num1
    while st < abs(step):
        nums *= num1
        st += 1

    return 1 / nums if step < 0 else nums


print('12, -3 = ', ro_milti(12, -3))
print('34, -8 = ', ro_milti(34, -8))
print('7 ,  5 = ', ro_milti(7, 5))

# ---------- 5 -------------------

sum_all = 0
ok_inp = True
while ok_inp:
    text = input('Введите числа разделенные пробелом. Выход = любая буква.  : ')
    list_txt = text.split()

    for stro in list_txt:
        try:
            tmp_sum = float(stro)
            sum_all += tmp_sum
        except:
            ok_inp = False
            break

print('Общая сумма чисел = ', sum_all)


# -----------  6 ---------------------------------
def ro_Txt(txt):
    return txt.title()


result = ''
for txt in 'home sweet home on the hill'.split():
    result += ro_Txt(txt) + ' '

print(result)
