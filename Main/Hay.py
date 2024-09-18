def harvest_hay():
	go_to_zero()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			try_harvest()
			ground_change(Grounds.Turf)
			move(North)
		move(East)
		