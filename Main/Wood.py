def harvest_wood():
	go_to_zero()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if ((get_pos_x()%2 == 0 and get_pos_y()%2 == 0) or (get_pos_x()%2 == 1 and get_pos_y()%2 == 1)):	
				try_harvest()
				plant(Entities.Tree)
			else:
				try_harvest()
				plant(Entities.Bush)
			move(North)
		move(East)