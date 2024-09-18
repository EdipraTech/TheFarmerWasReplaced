def harvest_carrots():
	go_to_zero()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			ground_change(Grounds.Soil)
			try_harvest()
			trade_items(Items.Carrot_Seed, get_world_size() **2)
			plant(Entities.Carrots)
			move(North)
		move(East)