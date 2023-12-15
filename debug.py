total = 0
symbol_format_info = []
number_format_info = []
pointers = []
generated_list = []
sharp_position = []
original_sharp_position = []
group_position = []
group_dict = {}


def recursion(index, case_index, layer):
	global symbol_format_info, generated_list, sharp_position, unknown_position, group_position, group_dict, original_sharp_position
	if index == len(sharp_position) - 1:
		# print(1)
		return len(symbol_format_info[case_index]) - sharp_position[index][1]
	
	answer = 0
	# print('topic', sharp_position)
	while True:
		if sharp_position[index + 1][0] - sharp_position[index][1] < 2:
			break
		if sharp_position[index][0] != 0 and symbol_format_info[case_index][sharp_position[index][0] - 1] == '#':
			break
		if sharp_position[-1][1] >= len(symbol_format_info[case_index]):
			break
		ans = 0
		for element_index in range(sharp_position[index][1], sharp_position[index + 1][0] - 1):
			if symbol_format_info[case_index][element_index] != '.':
				if element_index != sharp_position[index][1] and symbol_format_info[case_index][sharp_position[index][0] + element_index - sharp_position[index][1] - 1] == '#':
					break
				ans += 1
			else:
				break
		if ans == 0:
			break
		answer += ans * recursion(index + 1, case_index, layer + 1)
		temp_num = 0
		for element_index in range(sharp_position[index][0], len(symbol_format_info[case_index])):
			if symbol_format_info[case_index][element_index] != '?':
				temp_num = element_index
				break
			temp_num += 1
		if temp_num >= sharp_position[index][1] - sharp_position[index][0] + 1:
			# print(layer, '-----------------')
			original_position = [i for i in sharp_position[index]]
			bool_value = False
			for top_index in range(index, len(sharp_position)):
				if top_index == index:
					element_index = sharp_position[top_index][1] + ans
				else:
					element_index = sharp_position[top_index - 1][1] + 2
				top_bool = True
				while element_index < len(symbol_format_info[case_index]):
					if symbol_format_info[case_index][element_index] != '.':
						if symbol_format_info[case_index][element_index - sharp_position[top_index][1] + sharp_position[top_index][0]] == '#':
							top_bool = False
							break
						temp_num = 0
						for temp_index in range(element_index, element_index - (sharp_position[top_index][1] - sharp_position[top_index][0] + 1), -1):
							if symbol_format_info[case_index][temp_index] == '.':
								break
							temp_num += 1
						if temp_num < sharp_position[top_index][1] - sharp_position[top_index][0] + 1:
							element_index += 1
							continue
						length = sharp_position[top_index][1] - sharp_position[top_index][0] + 1
						sharp_position[top_index][1] = element_index
						sharp_position[top_index][0] = element_index - length + 1
						break
					element_index += 1
				# print(sharp_position)
				if top_index != len(sharp_position) - 1 and sharp_position[top_index + 1][0] - sharp_position[top_index][1] >= 2:
					bool_value = True
					break
				if top_bool is False:
					break
			if original_position == sharp_position[index]:
				break
			if sharp_position[-1][0] - sharp_position[-2][1] >= 2:
				bool_value = True
			if bool_value is False:
				break
		else:
			break
	
	sharp_position[index + 1][0] = original_sharp_position[index + 1][0]
	sharp_position[index + 1][1] = original_sharp_position[index + 1][1]
	
	sharp_position[index][0] = original_sharp_position[index][0]
	sharp_position[index][1] = original_sharp_position[index][1]
	return answer


def loop_order(case_index):
	global pointers, generated_list, number_format_info, symbol_format_info, sharp_position, group_position, group_dict, original_sharp_position
	generated_list = []
	for index in range(len(number_format_info[case_index])):
		length = number_format_info[case_index][index]
		for element in range(length):
			generated_list.append('#')
		if index < len(number_format_info[case_index]) - 1:
			generated_list.append('.')
	
	index = 0
	while index < len(symbol_format_info[case_index]):
		if symbol_format_info[case_index][index] == '?':
			break
		if symbol_format_info[case_index][index] != generated_list[index]:
			del symbol_format_info[case_index][index]
		else:
			index += 1
	length = len(symbol_format_info[case_index]) - len(generated_list)
	index = len(symbol_format_info[case_index]) - 1
	while index >= 0:
		if symbol_format_info[case_index][index] == '?':
			break
		if symbol_format_info[case_index][index] != generated_list[index - length]:
			del symbol_format_info[case_index][index]
			length -= 1
		index -= 1
	
	# print(generated_list)
	
	# Use a list store each group's range
	sharp_position = []
	temp_bool = False
	for index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][index] != '.':
			if temp_bool is False:
				temp_bool = True
				sharp_position.append([index])
		else:
			if temp_bool is True:
				temp_bool = False
				sharp_position[-1].append(index - 1)
	if temp_bool is True:
		temp_bool = False
		sharp_position[-1].append(len(symbol_format_info[case_index]) - 1)
	# print(sharp_position)
	
	index = 0
	layer = 0
	group_index = 0
	while index < len(generated_list):
		if generated_list[index] == '#':
			length = 0
			element_index = index
			while element_index < len(symbol_format_info[case_index]):
				if element_index + number_format_info[case_index][layer] - 1 > sharp_position[group_index][1]:
					group_index += 1
					element_index = sharp_position[group_index][0]
					continue
				if symbol_format_info[case_index][element_index] != '.':
					length = element_index - index
					break
				element_index += 1
			for element in range(length):
				generated_list.insert(index, '.')
			index += length + number_format_info[case_index][layer] - 1
			layer += 1
		index += 1
	
	sharp_position = []
	temp_bool = False
	for element_index in range(len(generated_list)):
		if generated_list[element_index] == '#':
			if temp_bool is False:
				temp_bool = True
				sharp_position.append([element_index])
		else:
			if temp_bool is True:
				temp_bool = False
				sharp_position[-1].append(element_index - 1)
	if temp_bool is True:
		temp_bool = False
		sharp_position[-1].append(len(generated_list) - 1)
	print(symbol_format_info[case_index])
	print(generated_list)
	index = 0
	while index < len(symbol_format_info[case_index]):
		if symbol_format_info[case_index][index] == '#' and (index >= len(generated_list) or (index < len(generated_list) and generated_list[index]  == '.')):
			end = 0
			for element_index in range(index, len(symbol_format_info[case_index])):
				if symbol_format_info[case_index][element_index] == '#':
					end = element_index
				else:
					break
			start = 0
			for element_index in range(index, -1, -1):
				if symbol_format_info[case_index][element_index] == '#':
					start = element_index
				else:
					break
			temp_index = start
			print(start, end)
			while True:
				sharp_index_end = 0
				for element_index in range(temp_index - 1, -1, -1):
					if generated_list[element_index] == '#':
						sharp_index_end = element_index
						break
				sharp_index_start = 0
				for element_index in range(len(sharp_position)):
					if sharp_index_end == sharp_position[element_index][1]:
						sharp_index_start = sharp_position[element_index][0]
						break
				print(sharp_index_start, sharp_index_end)
				if sharp_index_end - sharp_index_start + 1 < end - start + 1:
					temp_index = sharp_index_start
					continue
				break
			print("-----------------")
			temp_bool = False
			while temp_bool is False:
				generated_list.insert(sharp_index_start, '.')
				temp_bool = True
				for element_index in range(end, start - 1, -1):
					if len(generated_list) <= element_index:
						break
					if generated_list[element_index] != '#':
						temp_bool = False
						break
		index += 1
	# 	if symbol_format_info[case_index][index] == '#' and (index >= len(generated_list) or (index < len(generated_list) and generated_list[index] != '#')):
	# 		end = 0
	# 		for element_index in range(index, len(symbol_format_info[case_index])):
	# 			if symbol_format_info[case_index][element_index] == '#':
	# 				end = element_index
	# 			else:
	# 				break
	# 		start = 0
	# 		for element_index in range(index, -1, -1):
	# 			if symbol_format_info[case_index][element_index] == '#':
	# 				start = element_index
	# 			else:
	# 				break
	# 		group_index = -1
	# 		for element_index in range(index - 1, -1, -1):
	# 			if element_index >= len(generated_list):
	# 				continue
	# 			if generated_list[element_index] == '#':
	# 				temp_bool = True
	# 				group_index = element_index
	# 				break
	# 		for temp_index in range(len(sharp_position)):
	# 			if sharp_position[temp_index][1] == group_index:
	# 				group_index = temp_index
	# 				break
	# 		temp_bool = False
	# 		print(group_index)
	# 		print("--------------------------------")
	# 		print("--------------------------------")
	# 		while temp_bool is False:
	# 			print(symbol_format_info[case_index])
	# 			print(generated_list)
	# 			print(sharp_position)
	# 			print(group_index)
	# 			print("-------")
	# 			temp_bool = True
	# 			for element_index in range(sharp_position[group_index][1], end - 1):
	# 				if element_index != sharp_position[group_index][1] and symbol_format_info[case_index][
	# 					sharp_position[group_index][0] + element_index - sharp_position[group_index][1] - 1] == '#':
	# 					temp_bool = False
	# 					break
	# 			if temp_bool is False:
	# 				group_index -= 1
	# 		length = end - sharp_position[group_index][1]
	# 		for element in range(length):
	# 			generated_list.insert(sharp_position[group_index][0], '.')
	# 		sharp_position[group_index][0] += length
	# 		sharp_position[group_index][1] += length
	# 		for element in range(length):
	# 			if sharp_position[group_index][1] + 1 >= len(generated_list):
	# 				break
	# 			del generated_list[sharp_position[group_index][1] + 1]
	# 	index += 1
	#
	# while index < len(sharp_position) - 1:
	# 	if sharp_position[index + 1][0] - sharp_position[index][1] == 1:
	# 		generated_list.insert(sharp_position[index][1] + 1, '.')
	# 		sharp_position[index + 1][0] += 1
	# 		sharp_position[index + 1][1] += 1
	# 	index += 1
	
	group_position = []
	temp_bool = False
	temp_bool_all_questions = True
	for element_index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][element_index] != '.':
			if temp_bool is False:
				temp_bool = True
				temp_bool_all_questions = True
				group_position.append([element_index])
			if symbol_format_info[case_index][element_index] != '?':
				temp_bool_all_questions = False
		else:
			if temp_bool is True:
				temp_bool = False
				group_position[-1].append(element_index - 1)
				group_position[-1].append(temp_bool_all_questions)
	if temp_bool is True:
		temp_bool = False
		group_position[-1].append(len(symbol_format_info[case_index]) - 1)
		group_position[-1].append(temp_bool_all_questions)
	
	group_dict = {}
	
	for index in range(len(sharp_position)):
		for element_index in range(len(group_position)):
			if sharp_position[index][0] >= group_position[element_index][0] and sharp_position[index][1] <= group_position[element_index][1]:
				group_dict[index] = element_index
				break
	
	original_sharp_position = [[element for element in group] for group in sharp_position]
	
	# print(symbol_format_info[case_index])
	# print(generated_list)
	# print(group_dict)
	
	return 0
	# return recursion(0, case_index, 0)


with (open("2023/input/input12.txt", "r") as input_file):
	for line in input_file:
		temp = line.strip().split(' ')
		symbol_format_info.append([])
		number_format_info.append([])
		for copy in range(5):
			for element in list(temp[0]):
				symbol_format_info[-1].append(element)
			if copy < 4:
				symbol_format_info[-1].append('?')
			for element in temp[1].split(','):
				number_format_info[-1].append(int(element))
	
	for case in range(len(symbol_format_info)):
		decide = False
		pointers.append([])
		for element_index in range(len(symbol_format_info[case])):
			element = symbol_format_info[case][element_index]
			if element == '?' or element == '#':
				if decide is False:
					pointers[-1].append([element_index])
					decide = True
			else:
				if decide is True:
					pointers[-1][-1].append(element_index - 1)
					decide = False
		if decide:
			pointers[-1][-1].append(len(symbol_format_info[case]) - 1)
	for case in range(len(symbol_format_info)):
		a = total
		total += loop_order(case)
		# print(total - a)
		# print()
		# print()

print(total)