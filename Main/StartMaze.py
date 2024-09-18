def start_maze():
    clear()
    go_to_zero()
    while(num_items(Items.Pumpkin) < 1000):
        harvest_pumpkin_reset()
    plant(Entities.Bush)
    while not is_over(Entities.Hedge) and not is_over(Entities.Treasure):
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
	brute_force()