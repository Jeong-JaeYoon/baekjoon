x, y, w, h = map(int, input().split())
tmp_x = w-x
tmp_y = h-y

print(min(x, y, tmp_x, tmp_y))

