def count_words(text: str) -> int:
    return len(text.split())


def get_count_dict(text: str) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for char in text:
        lower_char: str = char.lower()
        if lower_char in count_dict:
            count_dict[lower_char] += 1
        else:
            count_dict[lower_char] = 1
    return count_dict


def sort_dict(count_dict):
    sorted_list = []
    for key, value in count_dict.items():
        sorted_list.append({"char": key, "num": value})

    def sort_on(d):
        return d["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
