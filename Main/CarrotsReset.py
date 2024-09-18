def harvest_carrots_reset():
	go_to_zero()
	while((num_items(Items.Hay) < get_world_size()*12 **2) and (num_items(Items.Wood) < get_world_size()*12 **2)):
		harvest_hay()
		harvest_wood_reset()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			ground_change(Grounds.Soil)
			try_harvest()
			trade_items(Items.Carrot_Seed, get_world_size() **2)
			plant(Entities.Carrots)
			move(North)
		move(East)