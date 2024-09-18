def clear_grid():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)
		move(East)
	
def try_harvest():
	while not can_harvest():
		if get_entity_type() == None:
			break
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
	harvest()
			
def is_over(ground):
	if get_entity_type() == ground:
		return True
	else:
		return False

def ground_change(ground):
	if get_ground_type() != ground:
		till()
		
def trade_items(trade_item, total_items):
	if num_items(trade_item) == 0:
		trade(trade_item, total_items)