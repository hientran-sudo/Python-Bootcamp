from data import menu, report, coin
from report import Report
from moneymachine import MoneyMachine
from coffeemaker import CoffeeMaker

new_report = Report()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

on = True
while on:
  new_report.print_report()
  selected_drink = input("\n\n*** What would you like (espresso/latte/cappuccino) ")
  
  if coffee_maker.check_ingredients(selected_drink):
    money_machine.check_money(selected_drink)
    
  selected_off = input("\n\n*** Turn off ? y/n ")
  if selected_off == "y":
    on = False
print("\nGood Bye")
