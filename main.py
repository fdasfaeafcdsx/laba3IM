import random
import math

def main():
    random.seed()
    balance = 10000
    warehouse_stock = 80
    transport_load = 0
    store_inventory = 30

    for simulation_time in range(101):
        print(f"\nТекущее время симуляции: {simulation_time}/100")
        print(f"Баланс счета: {balance} руб.")

        lot_size = 25 + random.randint(0, 30)
        unit_price = (40 + random.randint(0, 25)) + round(30.0 * simulation_time * (0.02 + 0.015 * random.randint(0, 1)))
        lot_cost = lot_size * unit_price
        print(f"Партия: {lot_size} шт.\nЦена за единицу: {unit_price} руб.\nОбщая стоимость: {lot_cost} руб.")
        purchase_decision = int(input("Закупить товар? (1 - Да, 0 - Нет): "))

        print(f"Склад: {warehouse_stock}/500 ед.\nГруз в пути: {transport_load}/100 ед.\nЗапасы в магазине: {store_inventory}/100 ед.")
        transport_decision = False

        if not transport_load:
            transport_decision = int(input("Перевозить товар? (1 - Да, 0 - Нет): "))
            if transport_decision:
                transfer_volume = int(input("Укажите объем перевозки [15 - 100]: "))

        sale_decision = int(input("Продать товар? (1 - Да, 0 - Нет): "))

        if purchase_decision:
            if lot_cost <= balance:
                balance -= lot_cost
                warehouse_stock = min(500, warehouse_stock + lot_size)

        if transport_decision:
            if transport_load:
                store_inventory = min(100, store_inventory + transport_load)
                transport_load = 0
            else:
                if warehouse_stock - transfer_volume > 0:
                    transport_load = transfer_volume
                    warehouse_stock -= transfer_volume
                else:
                    transport_load = warehouse_stock
                    warehouse_stock = 0

        if sale_decision:
            retail_price = int(input("Укажите цену продажи [90 - 210]: "))
            demand = round((25 + random.randint(0, 20)) * (1.0 - (1.0 / (1 + math.exp(-0.06 * (retail_price - 110))))))
            print(f"Ожидаемый спрос: {demand} шт.")
            if store_inventory > demand:
                store_inventory -= demand
                balance += retail_price * demand
            else:
                balance += retail_price * store_inventory
                store_inventory = 0

        print("=====================")

if __name__ == "__main__":
    main()
