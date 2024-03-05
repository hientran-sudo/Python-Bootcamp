from data import menu, report, coin

class CoffeeMaker:
  # Make coffee
  def make_coffee(self, selected_drink):
    for key in menu[selected_drink]['ingredients']:
      report[key] = report[key] - menu[selected_drink]['ingredients'][key]
    print("\n--- Here is your coffee. Enjoy! ---")

  # Check ingredient
  def check_ingredients(self, selected_drink):
    for key in menu[selected_drink]['ingredients']:
      if report[key] < menu[selected_drink]['ingredients'][key]:
        print(f"need more {key}")
        return False
    return True
