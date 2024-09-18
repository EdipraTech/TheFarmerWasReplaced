def harvest_wood_reset():
	go_to_zero()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if ((get_pos_x()%2 == 0 and get_pos_y()%2 == 0) or (get_pos_x()%2 == 1 and get_pos_y()%2 == 1)):	
				try_harvest()
				if num_unlocked(Unlocks.Trees) > 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
			else:
				try_harvest()
				plant(Entities.Bush)
			move(North)
		move(East)