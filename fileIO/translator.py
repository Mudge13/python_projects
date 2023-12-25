from translate import Translator

translator = Translator(to_lang="ja")
# translation = translator.translate("This is a pen.")
# print(translation)

with open("translator.txt", mode="r") as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)

    with open("translation_ja.txt", mode="w", encoding="utf-8") as ja_file:
        ja_file.write(translation)
