total = 0
list_str_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open("../../Documents/GitHub/Advent-of-Code/2023/input/input1.txt", "r") as file_input:
	for content in file_input:
		front = [-1]
		back = [-1]
		for str_num in list_str_num.keys():
			index = content.find(str_num)
			if index == -1:
				continue
			if front == [-1] or front[0] > index:
				front = [index, list_str_num[str_num]]
			if back == [-1] or back[0] < index:
				back = [index, list_str_num[str_num]]
		
		# print(front, back)
		calibration_value = 0
		index_front = -1
		index_back = -1
		temp = 0
		for step in range(0, len(content)):
			try:
				temp = int(content[step])
				if temp == 0:
					continue
				index_front = step
				break
			except ValueError:
				pass
		calibration_value *= 10
		for step in range(len(content) - 1, -1, -1):
			try:
				temp = int(content[step])
				if temp == 0:
					continue
				index_back = step
				break
			except ValueError:
				pass
		
		if index_front == -1 and front != [-1]:
			calibration_value = front[1]
		elif front == [-1] and index_front != -1:
			calibration_value = int(content[index_front])
		else:
			if index_front < front[0]:
				calibration_value = int(content[index_front])
			elif index_front > front[0]:
				calibration_value = front[1]
		
		calibration_value *= 10
		
		if index_back == -1 and back[0] != [-1]:
			calibration_value += back[1]
		elif back == [-1] and index_back != -1:
			calibration_value += int(content[index_back])
		else:
			if index_back > back[0]:
				calibration_value += int(content[index_back])
			elif index_back < back[0]:
				calibration_value += back[1]
		total += calibration_value

print(total)