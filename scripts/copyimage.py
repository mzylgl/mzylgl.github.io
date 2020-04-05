#!/usr/bin/env python

import os
import re
import sys
import shutil
from datetime import datetime


if __name__ == "__main__":
	# 复制 content\post目录下的图片 到 static目录下
	# content\post\2020\04\images\*  -> static\images\2020\04\*
	# 只会复制格式为 \YYY\MM\images 目录的图片， 其他目录会忽略

	img_folder_name = "images"
	cwd = os.getcwd()
	post_img_base_dir = os.path.join(cwd, "content", "post")
	static_img_base_dir = os.path.join(cwd, "static", img_folder_name)
	print("current work dir:", cwd)
	print("post_img_base_dir:", post_img_base_dir)
	print("static_img_base_dir:", static_img_base_dir)

	sep = os.path.sep
	sep_temp = r"\\" if sep == "\\" else sep
	pattern_str = sep_temp.join([r"\d{4}", r"\d{2}", img_folder_name])
	print("match pattern_str:", pattern_str, sep_temp)
	pattern = re.compile(pattern_str)      

	for root_dir, sub_dirs, file_names in os.walk(post_img_base_dir):
		print("walk '{}'".format(root_dir), end=" ")
		image_date_dir = sep.join(root_dir.split(sep)[-3:])  # 最后三个 2020\04\images
		if not pattern.match(image_date_dir):
			print("not match, continue.")
			continue
		else:
			print("match, copy images...")

		data_dir_items = image_date_dir.split(sep)[:2]  # 前两个 2020\04
		destination_dir = os.path.join(static_img_base_dir, *data_dir_items)

		if os.path.exists(destination_dir):
			print("    rm old '{}' ".format(destination_dir))
			shutil.rmtree(destination_dir)
		print("    copy '{}' to '{}' ".format(root_dir, destination_dir))
		shutil.copytree(root_dir, destination_dir)  # default use copy2
