from data import menu, report, coin

class Report:
  # Print report
  def print_report(self):
    selected_report = input("\n*** Do you want a report? y/n ")
    if selected_report == 'y':
      print(f"\n{report}")
