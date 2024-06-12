# 对联小工具

class Couplet:
    def __init__(self):
        self._up = None  # type:str
        self._down = None  # type:str

    def set_up(self, up):
        self._up = up

    def set_down(self, down):
        self._down = down

    @staticmethod
    def from_str(couplet_str):
        couplet = Couplet()
        up, down = couplet_str.split("\n")
        couplet.set_up(up)
        couplet.set_down(down)
        return couplet

    @staticmethod
    def from_strs(up, down):
        couplet = Couplet()
        couplet.set_up(up)
        couplet.set_down(down)
        return couplet

    @property
    def up(self):
        return self._up

    @property
    def down(self):
        return self._down


class CoupletDataStore:
    def __init__(self, couplets):
        self._couplets = couplets  # type:[Couplet]


class CoupletTool:

    @staticmethod
    def from_file(up_path, down_path):
        couplets = []  # type:[Couplet]
        with open(up_path, 'r', encoding='utf-8') as up_file:
            with open(down_path, 'r', encoding='utf-8') as down_file:
                while True:
                    up = up_file.readline().strip().replace(' ', '')
                    down = down_file.readline().strip().replace(' ', '')
                    if not up or not down:
                        break
                    couplets.append(Couplet.from_strs(up, down))
        return couplets

    @staticmethod
    def from_whole_file(path):
        """从完整的文件解析对联列表"""
        couplets = []
        with open(path, 'r', encoding='utf-8') as f:
            while True:
                couplet_str = f.readline()
                if couplet_str:
                    up, down = couplet_str.split(' ')
                    couplets.append(Couplet.from_strs(up, down))
                else:
                    break
        return couplets
