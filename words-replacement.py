import pandas as pd


def read_inflections_file() -> dict:
    df = pd.read_csv("curated-sources/all_inflections_modified.csv")
    return df.to_dict(orient="records")


def replace_ebts_file():
    # diff_dict = read_differences_file()
    inflections_dict = read_inflections_file()
    
    with open("original-sources/ebts.txt", "r") as ebts_file:
        ebts_data = ebts_file.read()
        ebts_data = ebts_data.replace("\n", " \n ")
    ebts_data_list = list(ebts_data.split(" "))

    for inflection_words in inflections_dict:
        for ebts_data_word in ebts_data_list:
            if inflection_words["inflection"] == ebts_data_word.lower():
                if inflection_words["headwords"] != ebts_data_word.lower():
                    index = ebts_data_list.index(ebts_data_word)
                    ebts_data_list[index] = inflection_words["headwords"]
                    print(f"{ebts_data_word} -> {ebts_data_list[index]} REPLACED!")
                else:
                    print(f"No replacement for ...... {ebts_data_word}!")
                    

    ebts_data = " ".join(ebts_data_list)
    ebts_data = ebts_data.replace(" \n ", "\n")

    with open("curated-sources/ebts_REPLACED.txt", "w") as ebts_replaced_file:
        ebts_replaced_file.write(ebts_data)


replace_ebts_file()
