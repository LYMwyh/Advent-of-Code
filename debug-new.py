total = 0
symbol_format_info = []
number_format_info = []
pointers = []
generated_list = []
sharp_position = []
original_sharp_position = []
group_position = []
group_dict = {}
positions = []
new_position = []
sharp_sum = []


def recursion(index, case_index):
	global symbol_format_info, generated_list, sharp_position, group_position, group_dict, original_sharp_position, \
		positions, new_position, sharp_sum
	answer = 0
	if index == len(sharp_position) - 1:
		temp_index = -1
		temp_bool = False
		new_position[index][1] = len(positions[index]) - 1
		# print(index, new_position[index][0], new_position[index][1])
		if index != 0:
			for element_index in range(new_position[index][0], new_position[index][1] + 1):
				if positions[index][element_index][0] - 1 >= 0 and sharp_sum[positions[index][element_index][0] - 1] - \
						sharp_sum[
							positions[index - 1][new_position[index - 1][1]][1]] > 0:
					temp_bool = True
					break
				else:
					temp_index = element_index
		elif index == 0:
			for element_index in range(new_position[index][0], new_position[index][1] + 1):
				if positions[index][element_index][0] - 1 >= 0 and sharp_sum[
					positions[index][element_index][0] - 1] > 0:
					temp_bool = True
					break
				else:
					temp_index = element_index
		if temp_index == -1 and temp_bool is True:
			return 0
		elif temp_index == -1 and temp_bool is False:
			pass
		else:
			new_position[index][1] = temp_index
		
		answer = new_position[index][1] - new_position[index][0] + 1
		# print(index, new_position[index][0], new_position[index][1], temp_index)
		# print(index, "answer", answer)
		return answer
	while True:
		new_position[index][1] = len(positions[index]) - 1
		
		temp_bool = True
		while temp_bool is True:
			for element_index in range(len(positions[index + 1])):
				if positions[index + 1][element_index][0] - positions[index][new_position[index][0]][1] >= 2:
					new_position[index + 1][0] = element_index
					break
			if sharp_sum[positions[index + 1][new_position[index + 1][0]][0] - 1] - sharp_sum[
				positions[index][new_position[index][0]][1]] == 0:
				break
			
			new_position[index][0] += 1
			if new_position[index][0] > new_position[index][1]:
				temp_bool = False
				break
		
		if temp_bool is False:
			break
		
		temp_index = -1
		for element_index in range(new_position[index][0], new_position[index][1] + 1):
			if positions[index + 1][new_position[index + 1][0]][0] - positions[index][element_index][1] >= 2:
				temp_index = element_index
			else:
				break
		# print(index, new_position[index][0], new_position[index][1], temp_index)
		if temp_index == -1:
			break
		
		new_position[index][1] = temp_index
		temp_index = -1
		temp_bool = False
		if index != 0:
			for element_index in range(new_position[index][0], new_position[index][1] + 1):
				if positions[index][element_index][0] - 1 >= 0 and sharp_sum[positions[index][element_index][0] - 1] - \
						sharp_sum[positions[index - 1][new_position[index - 1][1]][1]] > 0:
					temp_bool = True
					break
				else:
					temp_index = element_index
		elif index == 0:
			for element_index in range(new_position[index][0], new_position[index][1] + 1):
				if positions[index][element_index][0] - 1 >= 0 and sharp_sum[
					positions[index][element_index][0] - 1] > 0:
					temp_bool = True
					break
				else:
					temp_index = element_index
		if temp_index == -1 and temp_bool is True:
			break
		elif temp_index == -1 and temp_bool is False:
			pass
		else:
			new_position[index][1] = temp_index
		
		# print(index, new_position[index][0], new_position[index][1], temp_index)
		
		ans = new_position[index][1] - new_position[index][0] + 1
		
		if ans <= 0:
			break
		answer += ans * recursion(index + 1, case_index)
		# print(index, "answer", answer)
		if new_position[index][1] == len(positions[index]) - 1:
			break
		new_position[index][0] = new_position[index][1] + 1
	
	new_position[index + 1][0] = 0
	new_position[index + 1][1] = len(positions[index + 1]) - 1
	return answer


def alignment(start, end, case_index):
	global sharp_position, symbol_format_info, generated_list
	# print("---------")
	# print("question", end)
	# print(symbol_format_info[case_index])
	# print(generated_list)
	
	temp_index = end
	sharp_index_start = -1
	sharp_index_end = -1
	group_index = -1
	length = -1
	while True:
		sharp_index_end = 0
		for element_index in range(temp_index - 1, -1, -1):
			if element_index >= len(generated_list):
				continue
			if generated_list[element_index] == '#':
				sharp_index_end = element_index
				break
		sharp_index_start = -1
		for element_index in range(len(sharp_position)):
			if sharp_index_end <= sharp_position[element_index][1] and sharp_index_end >= sharp_position[element_index][
				0]:
				sharp_index_start = sharp_position[element_index][0]
				sharp_index_end = sharp_position[element_index][1]
				group_index = element_index
				break
		if sharp_index_end - sharp_index_start + 1 < end - start + 1:
			temp_index = sharp_index_start
			continue
		temp_bool = True
		
		temp_num = 0
		for element_index in range(start - 1, -1, -1):
			if symbol_format_info[case_index][element_index] == '#':
				temp_num += 1
			else:
				break
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		length = end - sharp_index_end
		for element_index in range(sharp_index_start, sharp_index_start + length):
			if symbol_format_info[case_index][element_index] == '#':
				temp_bool = False
				break
		
		if temp_bool is False:
			temp_start = -1
			temp_end = -1
			# print(sharp_index_start, sharp_index_end, temp_num, length)
			for element_index in range(sharp_index_start + length - 1, sharp_index_start - 1, -1):
				if symbol_format_info[case_index][element_index] == '#':
					if temp_bool is False:
						temp_bool = True
						temp_end = element_index
					temp_start = element_index
				elif temp_bool is True:
					break
			# print(temp_start, temp_end)
			alignment(temp_start, temp_end, case_index)
			sharp_index_start = sharp_position[group_index][0]
			sharp_index_end = sharp_position[group_index][1]
		if sharp_index_end - sharp_index_start + 1 <= end - start + temp_num + 1:
			length = end - sharp_index_end
		else:
			length = start - sharp_index_start
		length = end - sharp_index_end
		break
	if length >= 0:
		for element_index in range(length):
			generated_list.insert(sharp_index_start, '.')
		temp_index = -1
		temp_group = -1
		for element_index in range(group_index, len(sharp_position)):
			sharp_position[element_index][0] += length
			sharp_position[element_index][1] += length
			temp_index = sharp_position[element_index][1] + 1
			temp_group = element_index
			if element_index != len(sharp_position) - 1 and sharp_position[element_index + 1][0] - \
					sharp_position[element_index][1] >= 2:
				break
		
		for element_index in range(length):
			if temp_index >= len(generated_list) or temp_index < 0:
				break
			del generated_list[temp_index]
		
		for element_index in range(group_index + 1, temp_group + 1):
			length = sharp_position[element_index][0] - sharp_position[element_index - 1][1]
			for temp_index in range(length - 2):
				if temp_index >= len(generated_list) or temp_index < 0:
					break
				# print(generated_list)
				del generated_list[sharp_position[element_index - 1][1] + 1]
			sharp_position[element_index][0] -= length - 2
			sharp_position[element_index][1] -= length - 2
			if element_index != len(sharp_position) - 1:
				for temp_index in range(length - 2):
					generated_list.insert(sharp_position[element_index][1] + 1, '.')
	else:
		pass
	
	# print()
	
	for index in range(len(sharp_position)):
		length = 0
		while True:
			temp_bool = True
			for element_index in range(sharp_position[index][0], sharp_position[index][1] + 1):
				if symbol_format_info[case_index][element_index] == '.':
					temp_bool = False
					break
			if temp_bool is False:
				length += 1
				generated_list.insert(sharp_position[index][0], '.')
				sharp_position[index][0] += 1
				sharp_position[index][1] += 1
			else:
				break
		temp_index = sharp_position[index][1] + 1
		for element_index in range(index + 1, len(sharp_position)):
			if sharp_position[element_index][0] - sharp_position[element_index - 1][1] >= 2:
				break
			sharp_position[element_index][0] += length
			sharp_position[element_index][1] += length
			temp_index = sharp_position[element_index][1] + 1
		for element_index in range(length):
			# print(temp_index, len(generated_list))
			if temp_index < 0 or temp_index >= len(generated_list):
				break
			del generated_list[temp_index]
		
		if length > 0:
			for element_index in range(index, len(sharp_position) - 1):
				length = 0
				while sharp_position[element_index + 1][0] - sharp_position[element_index][1] - length > 2:
					del generated_list[sharp_position[element_index][1] + 1]
					length += 1
				for temp in range(element_index + 1, len(sharp_position)):
					sharp_position[temp][0] -= length
					sharp_position[temp][1] -= length


# print(generated_list)
# print("end")


def loop_order(case_index):
	global pointers, generated_list, number_format_info, symbol_format_info, sharp_position, group_position, group_dict, \
		original_sharp_position, positions, new_position, sharp_sum
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
	
	# print(symbol_format_info[case_index])
	# print(generated_list)
	
	temp_bool = False
	while temp_bool is False:
		temp_bool = True
		index = 0
		while index < len(symbol_format_info[case_index]):
			if symbol_format_info[case_index][index] == '#' and (
					index >= len(generated_list) or (index < len(generated_list) and generated_list[index] == '.')):
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
				alignment(start, end, case_index)
				temp_bool = False
			index += 1
	
	for index in range(len(sharp_position)):
		length = 0
		while True:
			temp_bool = True
			for element_index in range(sharp_position[index][0], sharp_position[index][1] + 1):
				if symbol_format_info[case_index][element_index] == '.':
					temp_bool = False
					break
			if temp_bool is False:
				length += 1
				generated_list.insert(sharp_position[index][0], '.')
				sharp_position[index][0] += 1
				sharp_position[index][1] += 1
			else:
				break
		temp_index = sharp_position[index][1] + 1
		for element_index in range(index + 1, len(sharp_position)):
			if sharp_position[element_index][0] - sharp_position[element_index - 1][1] >= 2:
				break
			sharp_position[element_index][0] += length
			sharp_position[element_index][1] += length
			temp_index = sharp_position[element_index][1] + 1
		
		for element_index in range(length):
			if temp_index < 0 or temp_index >= len(generated_list):
				break
			del generated_list[temp_index]
		
		if length > 0 and index != len(sharp_position) - 1:
			length = 0
			while sharp_position[index + 1][0] - sharp_position[index][1] - length > 2:
				del generated_list[sharp_position[index][1] + 1]
				length += 1
			for element_index in range(index + 1, len(sharp_position)):
				sharp_position[element_index][0] -= length
				sharp_position[element_index][1] -= length
	
	group_position = []
	temp_bool = False
	all_question = True
	for element_index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][element_index] != '.':
			if temp_bool is False:
				temp_bool = True
				all_question = True
				group_position.append([element_index])
			if symbol_format_info[case_index][element_index] != '?':
				all_question = False
		else:
			if temp_bool is True:
				temp_bool = False
				group_position[-1].append(element_index - 1)
				group_position[-1].append(all_question)
	if temp_bool is True:
		temp_bool = False
		group_position[-1].append(len(symbol_format_info[case_index]) - 1)
		group_position[-1].append(all_question)
	
	group_dict = {}
	
	for index in range(len(sharp_position)):
		for element_index in range(len(group_position)):
			if sharp_position[index][0] >= group_position[element_index][0] and sharp_position[index][1] <= \
					group_position[element_index][1]:
				group_dict[index] = element_index
				break
	
	original_sharp_position = [[element for element in group] for group in sharp_position]
	sharp_sum = [0 for i in range(len(symbol_format_info[case_index]))]
	for element_index in range(len(symbol_format_info[case_index])):
		if symbol_format_info[case_index][element_index] == '#':
			if element_index == 0:
				sharp_sum[element_index] = 1
			else:
				sharp_sum[element_index] = sharp_sum[element_index - 1] + 1
		else:
			if element_index != 0:
				sharp_sum[element_index] = sharp_sum[element_index - 1]
	
	print(symbol_format_info[case_index])
	print(generated_list)
	print(group_position)
	print(sharp_position)
	
	positions = [[] for i in range(len(sharp_position))]
	for index in range(len(sharp_position)):
		positions[index].append([i for i in sharp_position[index]])
		positions[index][-1].append(group_dict[index])
		if sharp_position[index][0] == 0:
			positions[index][-1].append(sharp_sum[sharp_position[index][1]])
		else:
			positions[index][-1].append(sharp_sum[sharp_position[index][1]] - sharp_sum[sharp_position[index][0] - 1])
	bool_value = True
	while bool_value:
		bool_value = False
		for index in range(len(sharp_position)):
			length = sharp_position[index][1] - sharp_position[index][0] + 1
			
			if index == len(sharp_position) - 1:
				group_index_end = len(group_position)
			else:
				group_index_end = positions[index + 1][-1][2] + 1
			for group_index in range(positions[index][-1][2], group_index_end):
				# if group_index != positions[index][-1][2] and group_position[positions[index][-1][2]][2] is False:
				# 	break
				# print(index, group_index)
				start = max(positions[index][-1][1] + 1, group_position[group_index][0] + length - 1)
				if index == len(positions) - 1:
					end = group_position[group_index][1] + 1
				else:
					end = min(positions[index + 1][-1][0] - 1, group_position[group_index][1] + 1)
				# print(index, start, end)
				if start >= end:
					continue
				# print(index, start, end)
				
				if group_index > positions[index][-1][2]:
					start += 1
					if group_position[group_index][0] == 0:
						positions[index].append(
							[group_position[group_index][0], group_position[group_index][0] + length - 1, group_index,
							 sharp_sum[group_position[group_index][0] + length - 1]])
					else:
						positions[index].append(
							[group_position[group_index][0], group_position[group_index][0] + length - 1,
							 group_index, sharp_sum[group_position[group_index][0] + length - 1] - sharp_sum[
								 group_position[group_index][0]]])
					bool_value = True
				
				for temp_index in range(start, end):
					if index != len(sharp_position) - 1 and positions[index + 1][-1][0] - temp_index < 2:
						break
					if symbol_format_info[case_index][temp_index] != '.':
						if temp_index - length + 1 == 0:
							positions[index].append(
								[temp_index - length + 1, temp_index, group_index, sharp_sum[temp_index]])
						else:
							positions[index].append(
								[temp_index - length + 1, temp_index, group_index,
								 sharp_sum[temp_index] - sharp_sum[temp_index - length]])
						bool_value = True
					else:
						break
	
	# for i in positions:
	# 	print(i)
	
	new_position = [[0, len(positions[index]) - 1] for i in range(len(sharp_position))]
	
	return 0
	# return recursion(0, case_index)


with (open("2023/input/input12.txt", "r") as input_file):
	# for line in input_file:
	# 	temp = line.strip().split(' ')
	# 	symbol_format_info.append(list(temp[0]))
	# 	number_format_info.append([int(element) for element in temp[1].split(',')])
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
		print(case)
		print(total - a)
# print()
# print()

print(total)

# ?###????????#
# . ###  ## #
