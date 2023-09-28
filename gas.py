import re

def give_all_stations():
    element_all_good = driver.find_elements(By.CLASS_NAME, good_st)
    element_all_bad = driver.find_elements(By.CLASS_NAME, bad_st)
    all = {'Station': []}
    for a in element_all_good:
        if len(a.text) > 0:
            r = a.text.split('\n')
            add = ''.join(' ' + char if char.isupper() else char.strip() for char in r[0]).strip()
            all['Station'].append(add)
    for a in element_all_bad:
        if len(a.text) > 0:
            r = a.text.split('\n')
            add = ''.join(' ' + char if char.isupper() else char.strip() for char in r[0]).strip()
            all['Station'].append(add)
    return all
