def solve_maze(iterations):
	if num_items(Items.Fertilizer) < iterations:
		trade(Items.Fertilizer, iterations*2 - num_items(Items.Fertilizer))
	count = 1
	dfs_arr = brute_force()
	if count < iterations:
		use_item(Items.Fertilizer)
		count +=1
	harvest()
	
def brute_force():
	posX = 0
	posY = 0
	dirs = [South, East, North, West]
	currDirection = 0
	newDirection = 0
	while get_entity_type() != Entities.Treasure:
		if get_pos_x() == posX and get_pos_y() == posY:
			currDirection +=1
			if currDirection >= 4:
				currDirection = 0
			posX = get_pos_x()
			posY = get_pos_y()
			move(dirs[currDirection])
		else:
			posX = get_pos_x()
			posY = get_pos_y()
			if currDirection-1 >= 0:
				newDirection = currDirection - 1
				move(dirs[newDirection])
			else:
				newDirection = 3
				move(dirs[newDirection])
			if get_pos_x() != posX or get_pos_y() != posY:
				currDirection = newDirection
			else:
				move(dirs[currDirection])
				
	harvest()
	#return curr_array