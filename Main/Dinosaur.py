def harvest_dinosaur():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if num_items(Items.Egg) == 0:
				trade_items(Items.Egg, get_world_size() **2)
			use_item(Items.Egg)
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)
		move(East)