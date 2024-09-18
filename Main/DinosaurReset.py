def harvest_dinosaur_reset():
	while (num_items(Items.Cactus) < get_world_size()*40 **2):
		harvest_cactus_reset()
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
			if num_items(Items.Bones) > 2000:
				unlock(Unlocks.Leaderboard)
				timed_reset()
			move(North)
		move(East)