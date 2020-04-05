#!/usr/bin/env python

import os
import sys
from datetime import datetime

if __name__ == "__main__":
	# 在blog目录下 执行 ./scripts/hugonew.py post/test.md
	# hugo new的时候同时创建当前时间的子文件夹
	# hugo new post/test.md  -> hugo new post/2020/04/test.md

	cwd = os.getcwd()
	print("current work dir:", cwd)

	cur_date_str = datetime.now().strftime("%Y-%m")
	cur_date_str_dir = os.path.join(*cur_date_str.split("-"))
	print("current date folder:", cur_date_str_dir)

	file_path = sys.argv[1]
	print("[hugo new] input file path:", file_path)

	if "/" in file_path:
		file_path_items = file_path.split("/")
	else:
		file_path_items = file_path.split("\\")
	print("[hugo new] input file path items:", file_path_items)

	date_file_path = os.path.join(file_path_items[0], cur_date_str_dir, *file_path_items[1:])
	# print(file_path_items[0], file_path, *file_path_items[1:])
	print("[hugo new] output file path:", date_file_path)

	cmd = "hugo new {}".format(date_file_path)
	print("exec cmd '{}'".format(cmd), "\n\n")
	sys.stdout.flush()

	os.system(cmd)
