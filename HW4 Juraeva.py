import re
with open('linguistics.txt', 'r', encoding="UTF-8") as f:
    text = f.read()

text = re.sub("язык([а-я]{0,3})([ -.,!?);»:\n/[\t])", r"шашлык\1\2", text)
new_text = re.sub("Язык([а-я]{0,3})([ -.,!?);»:\n/[\t])", r"Шашлык\1\2", text)
 
with open("test2", "w", encoding="UTF-8") as file_out:
    file_out.write(text)
    

	
with open('philosophy.txt', 'r', encoding="UTF-8") as f:
    text = f.read()
    text = new_text
new_text = re.sub("Философи([а-я]{0,3})([ -.,!?);»:\n/[\t])", r"Астрологи\1\2", new_text)
new_text = re.sub("философи([а-я]{1,3})([ -.,!?);»:\n/[\t])", r"астрологи\1\2", new_text)

with open("test3", "w", encoding="UTF-8") as file_out:
    file_out.write(new_text)
    


with open('phinland.txt', 'r', encoding="UTF-8") as f:
    text = f.read()
    
text = re.sub("Финлянди([а-я]{1,2})([ -.,!?);»:\n/[\t])", r"Малайзи\1\2", text)

with open("test4", "w", encoding="UTF-8") as file_out:
    file_out.write(text)