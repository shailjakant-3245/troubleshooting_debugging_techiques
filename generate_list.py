#!/usr/bin/env python3


def alphabet():
	list=[]
	for i in range(97,123):
		for j in range(97,123):
			for k in range(97,123):
				for l in range(1,2022):
					list.append(str(chr(i)+chr(j)+chr(k))+str(l))
	return sorted(list)


alphabet()