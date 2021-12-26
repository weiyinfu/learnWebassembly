import math
import random

import numpy as np
from js import document, console, window


def down(a: np.ndarray):
    for y in range(4):
        ans = []
        merged = False
        for x in range(3, -1, -1):
            if a[x][y]:
                if ans and ans[-1] == a[x][y] and not merged:
                    merged = True
                    ans[-1] *= 2
                else:
                    ans.append(a[x][y])
        while len(ans) < 4:
            ans.append(0)
        a[:, y] = ans[::-1]


def rotate(a: np.ndarray):
    b = np.empty_like(a)
    for i in range(4):
        for j in range(4):
            b[i][j] = a[j][3 - i]
    return b


def generate(a: np.ndarray):
    # 随机产生一个元素
    b = a.reshape(-1)
    ind = np.argwhere(b == 0).reshape(-1)
    b[ind[np.random.randint(0, len(ind))]] = 2


def rotate_many(a: np.ndarray, times: int):
    for i in range(times):
        a = rotate(a)
    return a


def no_same(a):
    # 判断是否存在相邻且相等的元素
    for i in range(4):
        for j in range(4):
            if i + 1 < 4 and a[i][j] == a[i + 1][j]:
                return False
            if j + 1 < 4 and a[i][j] == a[i][j + 1]:
                return False
    return True


def get_color_list(cnt):
    # 获取可用的颜色列表，在三维空间中均匀地选择若干个点
    a = []
    c = cnt ** (1 / 3)
    cc = math.ceil(c)

    def get(x):
        ans = hex(math.floor((x + 1) / cc * 255))[2:]
        if len(ans) < 2:
            return '0' + ans
        return ans

    for i in range(cc):
        for j in range(cc):
            for k in range(cc):
                now = f"#{get(i)}{get(j)}{get(k)}"
                a.append(now)
    # 保证每次颜色一致性
    random.seed(0)
    random.shuffle(a)
    return a[:cnt]


color_list = get_color_list(20)


def color2vec(s: str):
    # 颜色字符串转int数组
    a = np.array([int(s[i:i + 2], base=16) for i in range(1, len(s), 2)])
    return a


def get_fore(back_color: str):
    # 根据背景色距离黑白两色的距离来决定前景色使用黑色还是白色
    white_dis = np.linalg.norm(color2vec(back_color) - 255)
    black_dis = np.linalg.norm(color2vec(back_color) - 0)
    fore_color = 'white' if white_dis > black_dis else 'black'
    return fore_color


def get_color(v):
    # 返回前景色和背景色
    if v == 0:
        return 'white', 'black'
    ind = math.floor(math.log2(v))
    ind = np.clip(ind, 0, len(color_list))
    back_color = color_list[ind]
    return get_fore(back_color), back_color


class Game2048:
    def is_over(self) -> bool:
        return np.count_nonzero(self.a == 0) == 0 and no_same(self.a)

    def update(self, *args, **kwargs):
        grid_size = get_grid_size()
        console.log(f"gridSize={grid_size}")
        container.style.width = grid_size * 4
        for i in range(4):
            for j in range(4):
                v = self.a[i, j]
                fore, back = get_color(v)
                ele = document.querySelector(f'#div{i}{j}')
                if v == 0:
                    ele.opacity = 0
                    ele.innerText = ''
                    ele.style.backgroundColor = 'unset'
                    ele.style.color = 'unset'
                else:
                    ele.opacity = 1
                    ele.innerText = f"{v}"
                    ele.style.backgroundColor = back
                    ele.style.color = fore
                ele.style.width = grid_size
                ele.style.height = grid_size
        if self.game_over:
            console.log("click any key to continue")

    def on_cmd(self, cmd):
        cmd = cmd.key
        if self.game_over:
            if cmd in ('enter', 'Enter'):
                self.init()
            return
        ops = ["ArrowUp", 'ArrowRight', 'ArrowDown', 'ArrowLeft']
        if cmd not in ops:
            return
        ind = ops.index(cmd)
        times = (2 - ind + 4) % 4
        b = rotate_many(self.a, (4 - times) % 4)
        down(b)
        self.a = rotate_many(b, times)
        if np.count_nonzero(self.a == 0):
            generate(self.a)
        self.game_over = self.is_over()

    def init(self):
        self.a = np.zeros((4, 4), dtype=np.int32)
        self.game_over = False
        generate(self.a)


def play_sound(s: str):
    document.querySelector(f"#{s}").play()


def get_grid_size():
    rect = document.querySelector('body').getBoundingClientRect()
    return min(rect.width, rect.height) / 4


container = document.querySelector('#main')
cover = document.querySelector("#cover")
g = Game2048()
g.init()


class Sound:
    start = "start"
    over = "over"
    move = "move"


def show_cover():
    cover.style.display = 'flex'


def hide_cover():
    cover.style.display = 'none'


def onkeydown(event):
    console.log("keydown")
    console.log(event)
    last_over = g.game_over
    g.on_cmd(event)
    if not last_over and g.game_over:
        show_cover()
        play_sound(Sound.over)
    if last_over and not g.game_over:
        hide_cover()
        play_sound(Sound.start)
    g.update()


for i in range(16):
    x = i // 4
    y = i % 4
    div = document.createElement('div')
    div.id = f"div{x}{y}"
    div.className += " grid"
    container.appendChild(div)
document.onkeydown = onkeydown
window.onresize = lambda e: g.update()
g.update()
play_sound(Sound.start)
