from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pandas as pd 


opts = Options()

opts.headless=True


browser = Firefox(options=opts)  ## should include webdriver as arguement if webdriver not in /usr/local/bin/


categories = ['animal','color','country','food']


df = pd.DataFrame(columns=['Name', 'About', 'Category'])

for cat in categories:

    print(cat)
    print()


    file = open(cat+'.txt','r')
    lines = file.readlines()



    for line in lines:

        name = line[:-1]

        print(name)

        browser.get('https://en.wikipedia.org/wiki/'+name)


        try:
            texts = browser.find_elements_by_tag_name('p')
            text = texts[1].text
            text = text + ' '+ texts[2].text
            text = text + ' '+ texts[3].text
            text = text + ' '+ texts[4].text
            text = text + ' '+ texts[5].text
        except:
            continue     

        new_row = {'Name':name, 'About':text, 'Category':cat }

        df = df.append(new_row, ignore_index=True)

      

df.to_csv('data.csv')


browser.close()
