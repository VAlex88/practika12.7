per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита: "))
deposit = []
deposit.append(money*per_cent['ТКБ']/100)
deposit.append(money*per_cent['СКБ']/100)
deposit.append(money*per_cent['ВТБ']/100)
deposit.append(money*per_cent['СБЕР']/100)
print(deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать —", max_deposit)