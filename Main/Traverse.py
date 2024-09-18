def go_to_zero():
	if get_entity_type() != Entities.Hedge:
		while get_pos_x() > 0:
			move(East)
		while get_pos_y() > 0:
			move(North)