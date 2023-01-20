import webbrowser
from json import load, dump

import os

# file path
assets_tmp: str = rf'{os.getenv("tmp")}\assets'
data_tmp: str = rf'{assets_tmp}\\data.json'
favicon_tmp: str = rf'{assets_tmp}\\favicon.png'

data: list[dict] = [
        {"name_conf": "Математика",
         "url": "https://us04web.zoom.us/j/9690474107?pwd=bUpuYXFydklnaFFlRTI2VnFIOE5sZz09",
         'hide': False},
        {"name_conf": "Русский язык",
         "url": "https://us04web.zoom.us/j/73315543002?pwd=wlGKjsJHFWWDU2oPFeYqG4GOpKq5KK.1#success09",
         'hide': False},
        {"name_conf": "Английский язык",
         "url": "https://us04web.zoom.us/j/9330067214?pwd=YkxxTnVEcUtidWVNUno5MEtPRmkyUT09",
         'hide': False},
        {"name_conf": "История",
         "url": "https://us04web.zoom.us/j/2532973267?pwd=cFlNSmYxT3ZObzZBVTlHL0YzNFltdz09#success",
         'hide': False},
        {"name_conf": "Информатика",
         "url": "https://us04web.zoom.us/j/76870763158?pwd=8qz8L6RZga4qFK2t2gY6ESUla93nYR.1",
         'hide': False},
        {"name_conf": "Физика",
         "url": "https://us04web.zoom.us/j/2742436442?pwd=bG5OMmd1ZE4vcWRwVXFBcDEyQXl5UT09",
         'hide': False},
        {"name_conf": "ИП",
         "url": "https://us04web.zoom.us/j/2491069797?pwd=cDYxRkl5ejlGSkxaSFczeXh6R3FKZz09",
         'hide': False},
        {"name_conf": "Химия",
         "url": "https://us04web.zoom.us/j/7977029326?pwd=NWNYVEhmREh5VDN0TW40WnplVGQ3QT09",
         'hide': False},
        {"name_conf": "Физ-ра",
         "url": "https://us04web.zoom.us/j/78560559321?pwd=vBa3Sfs13I3ldbcmC7ielSO30Y8jFa.1#success",
         'hide': False},
        {"name_conf": "География",
         "url": "https://us05web.zoom.us/j/4544548111?pwd=VGhtcFl1OW14eTBreU9ULzByc2VYUT09",
         'hide': False}
]


class ZoomPlusConfig:
    def __init__(self):
        self.limit_buttons = 10  # base limit of button in window

        self.main_buttons = [f'btn_{i}' for i in range(self.limit_buttons)]
        self.main_shortcut = {f'btn_{i - 1}': f'Alt+{i}' for i in range(1, self.limit_buttons)} | {'btn_9': 'Alt+0'}
        self.main_lbl = [f'lbl_{i}' for i in range(self.limit_buttons)]
        self.main_le = [f'le_{i}' for i in range(self.limit_buttons)]

        # Setting files app
        if not os.path.exists(assets_tmp):
            os.mkdir(assets_tmp)
            self.create_data()
        elif not os.path.exists(data_tmp):
            self.create_data()

    @staticmethod
    def create_data(data_update=None):
        if data_update is None:
            data_update = data
        with open(rf'{assets_tmp}\\data.json', 'w') as file:
            dump(data_update, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read_data_conf() -> list[dict]:
        with open(rf'{assets_tmp}\\data.json', encoding='windows-1251') as file:
            return load(file)

    def open_url_conf(self, index: int) -> None:
        webbrowser.open(self.get_url_conf(index))

    def get_name_conf(self, index: int) -> str:
        data_read = self.read_data_conf()
        return data_read[index]['name_conf']

    def get_url_conf(self, index: int) -> str:
        return self.read_data_conf()[index]['url']

    def set_name_conf(self, value: str, index: int) -> None:
        data_read = self.read_data_conf()
        data_read[index]['name_conf'] = value
        self.create_data(data_read)

    def set_url_conf(self, value: str, index: int) -> None:
        data_read = self.read_data_conf()
        data_read[index]['url'] = value
        self.create_data(data_read)

    @property
    def get_count_actual_buttons(self) -> int:
        return sum(not e.get('hide') for e in self.read_data_conf())

    def check_hide(self, ind: int) -> bool:
        return self.read_data_conf()[int(ind)]['hide']

    def set_hide_button(self, ind: int) -> None:
        data_read = self.read_data_conf()
        data_read[ind]['hide'] = True
        self.create_data(data_read)

    # Future:

    def set_show_button(self, ind: int) -> None:
        data_read = self.read_data_conf()
        data_read[ind]['hide'] = False
        self.create_data(data_read)
