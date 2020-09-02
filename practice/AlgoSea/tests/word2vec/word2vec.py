# Step1：数据准备：
import jieba

user_def_words=['杨过','小龙女','郭靖','黄蓉','陆无双','程英','郭芙','郭襄','黯然销魂掌','打狗棒法','九阴真经','降龙十八掌','九阳真经','玉女心经']
for word in user_def_words:
    jieba.add_word(word, freq=20000)


with open("/Users/sunny_lin/Documents/study/github/nlp_sea/practice/AlgoSea/data/神雕侠侣.txt", "r", encoding="gbk") as f:
    all_text = f.readlines()

with open("/Users/sunny_lin/Documents/study/github/nlp_sea/practice/AlgoSea/data/sdxl.txt", "w", encoding="utf-8") as f:
    f.write("".join(all_text))

token_list = []
with open("/Users/sunny_lin/Documents/study/github/nlp_sea/practice/AlgoSea/data/sdxl.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        new_line = jieba.cut(line, cut_all=False)
        str = (" ".join(new_line).replace('，', '').replace('。', '').replace('！', '').replace('；', '').replace('：', '')
               .replace('「', '').replace('」', '').replace('、', '').replace('', '').replace('？', '').replace('『', '')
               .replace('』', '').replace('…', '').replace('( ', '').replace(') ', '').replace('《', '').replace('》', '')
               )
        token_list.append(str)
        line = f.readline()

print(token_list[0])