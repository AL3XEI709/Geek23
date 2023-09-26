scoreboard = []
while True:
    name = input()
    if name == "quit":
        break
    try:
        score = float(input())
    except ValueError:
        print("成绩必须是数字，请重新输入。")
        continue
    scoreboard.append((name, score))
scoreboard.sort(key=lambda x: x[1], reverse=True)

for i, (name, score) in enumerate(scoreboard):
    print(f"第{i+1}名：{name}, 成绩为{score}分")
