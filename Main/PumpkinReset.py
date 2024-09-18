def harvest_pumpkin_reset():
	go_to_zero()
	not_full = True
	while(num_items(Items.Carrot) < get_world_size()*6 **2):
		harvest_carrots_reset()
	while not_full:
		count = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				ground_change(Grounds.Soil)
				if can_harvest():
					count +=1
				trade_items(Items.Pumpkin_Seed, get_world_size() **2)
				plant(Entities.Pumpkin)
				use_item(Items.Water_Tank)
				move(North)
				if count == get_world_size() **2:
					try_harvest()
					not_full = False
				if get_entity_type() == Entities.Carrots or get_entity_type() == Entities.Bush:
					clear_grid()
			move(East)