def harvest_sunflower():
	go_to_zero()
	best_petals = 0
	best_position = None
	#new_arr = dict()
	position_x = []
	position_y = []
	petal_list = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				till()
			trade_items(Items.Sunflower_Seed, get_world_size() **2)
			if get_entity_type() != Entities.Sunflower:
				harvest()
			plant(Entities.Sunflower)
			use_item(Items.Water_Tank)
			if get_entity_type() == Entities.Sunflower:
				curr_petals = measure()
				if len(petal_list) == 0:
					petal_list.append(curr_petals)
					position_x.append(get_pos_x())
					position_y.append(get_pos_y())
				else:
					for i in range(len(petal_list)):
						if curr_petals >= petal_list[i]:
							petal_list.insert(i, curr_petals)
							position_x.insert(i, get_pos_x())
							position_y.insert(i, get_pos_y())
							break
						elif i == len(petal_list)-1:
							petal_list.append(curr_petals)
							position_x.append(get_pos_x())
							position_y.append(get_pos_y())
							break
				#if curr_petals > best_petals:
				#	best_petals = curr_petals
				#	best_position = (get_pos_x(), get_pos_y())
			move(North)
		move(East)
	farm_sunflower(position_x, position_y)
	
def farm_sunflower(x_pos, y_pos):
	for i in range(len(x_pos)):
		at_pos = False
		while not at_pos:
			if get_pos_x() < x_pos[i]:
				move(East)
			if get_pos_x() > x_pos[i]:
				move(West)
			if get_pos_y() < y_pos[i]:
				move(North)
			if get_pos_y() > y_pos[i]:
				move(South)
			if get_pos_x() == x_pos[i] and get_pos_y() == y_pos[i]:
				try_harvest()
				at_pos = True
		