# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data()->str:
    """Return content from the 10k_racetimes.txt file"""
    with open('./10k_racetimes.txt', 'rt') as file:
            content = file.read()
    return content

def get_rhines_times()->list:
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_list:list[str] = [t.split()[0] for t in races.split("\n")[1::] if "Jennifer Rhines" in " ".join(t.split()[1:3])]
    
    return rhines_list

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total=datetime.timedelta()

    for racetime in racetimes:
      try:
          min,sec,mel = re.split(r'[:.]',racetime)
          total+= datetime.timedelta(minutes=int(min),seconds=int(sec),milliseconds=int(mel))
      except ValueError:
        min,sec = re.split(r'[:]',racetime)
        total+= datetime.timedelta(minutes=int(min),seconds=int(sec))
    return f'{total/len(racetimes)}'[2:-5]


if __name__=="__main__":
    print(get_average())