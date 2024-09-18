def harvest_cactus_reset():
	harvested = False
	moved = 0
	while(num_items(Items.Gold) < get_world_size()*40 **2):
		start_maze()
	go_to_zero()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() != Entities.Cactus:
				try_harvest()
			ground_change(Grounds.Soil)
			trade_items(Items.Cactus_Seed, get_world_size() **2)
			plant(Entities.Cactus)
			move(North)
		move(East)
	while not harvested:
		moved = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if i == 0 and j == 0:
					if measure() > measure(North):
						swap(North)
						moved +=1
					if measure() > measure(East):
						swap(East)
						moved +=1
				if i == 0 and i < get_world_size()-1:
					if measure() > measure(North):
						swap(North)
						moved +=1
					if measure() > measure(East):
						swap(East)
						moved +=1
				if j == 0 and j < get_world_size()-1:
					if measure() > measure(North):
						swap(North)
						moved +=1
					if measure() > measure(East):
						swap(East)
						moved +=1
				if i < get_world_size()-1:
					if measure() > measure(East):
						swap(East)
						moved +=1
				if j < get_world_size()-1:
					if measure() > measure(North):
						swap(North)
						moved +=1
				move(North)
			move(East)
		if moved <= 2:
			harvested = True
			
	try_harvest()