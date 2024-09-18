def harvest_lowest_reset(confirm):
	while confirm == True:
		unlock(Unlocks.Speed)
		unlock(Unlocks.Grass)
		unlock(Unlocks.Expand)
		unlock(Unlocks.Plant)
		unlock(Unlocks.Carrots)
		unlock(Unlocks.Trees)
		unlock(Unlocks.Pumpkins)
		unlock(Unlocks.Fertilizer)
		unlock(Unlocks.Mazes)
		unlock(Unlocks.Sunflowers)
		unlock(Unlocks.Cactus)
		unlock(Unlocks.Sunflowers)
		unlock(Unlocks.Polyculture)
		unlock(Unlocks.Dinosaurs)
		if num_unlocked(Unlocks.Leaderboard) > 0:
			timed_reset()
		hay_count = num_items(Items.Hay)
		wood_count = 10000000
		if num_unlocked(Unlocks.Plant) > 0:
			wood_count = num_items(Items.Wood)
		carrot_count = 10000000
		if num_unlocked(Unlocks.Carrots) > 0:
			carrot_count = num_items(Items.Carrot)
		pumpkin_count = 10000000
		if num_unlocked(Unlocks.Pumpkins) > 0:
			pumpkin_count = num_items(Items.Pumpkin)
		power_count = 10000000
		if num_unlocked(Unlocks.Sunflowers) > 0:
			power_count = num_items(Items.Power)
		gold_count = 10000000
		if num_unlocked(Unlocks.Mazes) > 0:
			gold_count = num_items(Items.Gold)
		cactus_count = 10000000
		if num_unlocked(Unlocks.Cactus) > 0:
			cactus_count = num_items(Items.Cactus)
		bones_count = 10000000
		if num_unlocked(Unlocks.Dinosaurs) > 0:
			bones_count = num_items(Items.Bones)
		lowest = min(hay_count, wood_count, carrot_count, pumpkin_count, power_count, gold_count, cactus_count, bones_count)
		if lowest == hay_count:
			harvest_hay()
		elif lowest == wood_count:
			harvest_wood_reset()
		elif lowest == carrot_count:
			harvest_carrots_reset()
		elif lowest == pumpkin_count:
			harvest_pumpkin_reset()
		elif lowest == power_count:
			harvest_sunflower_reset()
		elif lowest == gold_count:
			start_maze()
		elif lowest == cactus_count:
			harvest_cactus_reset()
		elif lowest == bones_count:
			harvest_dinosaur_reset()