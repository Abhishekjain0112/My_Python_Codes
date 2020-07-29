def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = [group]
			else:
				user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)


def check_localhost():
	localhost = socket.gethostbyname('localhost')
	return localhost == "127.0.0.1"


def check_connectivity:
	request = requests.get("http://www.google.com")
	return request == 200

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))