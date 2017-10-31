def tower_move(disks, start, finish, middle):
	if disks>= 1:
		tower_move(disks- 1, start, middle, finish)
		# disk_move(start, finish)
		print("we moved the disk from:", start, "to", finish)
		tower_move(disks-1, middle, finish, start)

tower_move(3, "Tower A First", "Tower C Finish", "Tower B middle")


