def harvest_lowest(confirm):
	while confirm == True:
		hay_count = num_items(Items.Hay)
		wood_count = num_items(Items.Wood)
		carrot_count = num_items(Items.Carrot)
		pumpkin_count = num_items(Items.Pumpkin)
		power_count = num_items(Items.Power)
		gold_count = num_items(Items.Gold)
		cactus_count = num_items(Items.Cactus)
		bones_count = num_items(Items.Bones)
		lowest = min(hay_count, wood_count, carrot_count, pumpkin_count, power_count, gold_count, cactus_count, bones_count)
		if lowest == hay_count:
			harvest_hay()
		elif lowest == wood_count:
			harvest_wood()
		elif lowest == carrot_count:
			harvest_carrots()
		elif lowest == pumpkin_count:
			harvest_pumpkin()
		elif lowest == power_count:
			harvest_sunflower()
		elif lowest == gold_count:
			start_maze()
		elif lowest == cactus_count:
			harvest_cactus()
		elif lowest == bones_count:
			harvest_dinosaur()