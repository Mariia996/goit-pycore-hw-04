def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_lst = file.readlines()
            result = []
            for cat in cats_lst:
                f_cat = cat.split(",")
                dct_cat = {"id": f_cat[0], "name": f_cat[1], "age": f_cat[2].strip()}
                result.append(dct_cat)

            return result

    except FileNotFoundError:
        print("The File is not found!")
        return (None, None)
    except UnicodeDecodeError as e:
        print(f"The File cannot be decoded! Error: {e}")
        return (None, None)
    except Exception as e:
        print(f"Something went wrong! Error: {e}")
        return (None, None)


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
