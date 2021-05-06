import csv
import os

from jieba.analyse import *


# 定义有序字典
# import collections
# my_order_dict = collections.OrderedDict()

class HotComments:
    # 返回文件下的所有评论内容
    def get_comments(self, file_name):
        hot_comments = ''
        with open(file_name, encoding='utf-8') as f:
            reader = csv.reader(f)
            column = [row[2] for row in reader]
        # 将表头删除
        column.pop(0)
        for each in column:
            hot_comments += each
        return hot_comments

    def get_hot_comments(self, hot_comments):
        hot_words = {}
        for keyword, weight in textrank(hot_comments, topK=21, withWeight=True):
            hot_words[keyword] = weight
        return hot_words

    def write_into_csv(self, data, file_name):
        with open(file_name, 'w', newline='', encoding='utf-8-sig') as f:
            fieldnames = {'评论热词', '热度'}
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            [f.write('{0},{1}\n'.format(key, value)) for key, value in data.items() if value != 1]
            # for key, value in data:
            #     writer.writerow(rowdict={key: value})


if __name__ == '__main__':


    # 保存所有酒店名称列表
    flat_file_names = ''
    spot_file_names = ''
    # 用于路径拼接
    flat_file_dir = 'flatcomment'
    spot_file_dir = 'spotcomment'

    # 酒店信息
    for root, dirs, files in os.walk(flat_file_dir, topdown=False):
        # 遍历酒店名,temp_filename保存酒店名
        flat_file_names = files

    for temp_filename in flat_file_names:
        read_filename = os.path.join('flatcomment', temp_filename)
        save_filename = os.path.join('flatresult', temp_filename)
        if not os.path.exists('flatresult'):
            os.makedirs('flatresult')
        print(save_filename)
        test = HotComments()
        test.write_into_csv(test.get_hot_comments(test.get_comments(read_filename)), save_filename)

    # 景区信息
    for root, dirs, files in os.walk(spot_file_dir, topdown=False):
        # 遍历酒店名,temp_filename保存酒店名
        spot_file_names = files

    for temp_filename in spot_file_names:
        read_filename = os.path.join('spotcomment', temp_filename)
        save_filename = os.path.join('spotresult', temp_filename)
        if not os.path.exists('spotresult'):
            os.makedirs('spotresult')
        print(save_filename)
        test = HotComments()
        test.write_into_csv(test.get_hot_comments(test.get_comments(read_filename)), save_filename)
