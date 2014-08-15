# Test for the Fade algorithm

array_of_RGB_values = [[0,0,0]]
last_RGB_values = array_of_RGB_values.pop()
red = 55
green = 27
blue = 248

change_colors(last_RGB_values[0], last_RGB_values[1], last_RGB_values[2], red, green, blue)


def change_colors(old_red, old_green, old_blue, new_red, new_green, new_blue):
	# Torch color smooth transition between temperature settings
	print(old_red, old_green, old_blue)	
	print(new_red, new_green, new_blue)	
	
	while (old_red != new_red or old_blue != new_blue or old_green != new_green): 

		if old_red != new_red:
			if old_red < new_red:
				if old_red + 20 > new_red:
					old_red = new_red
				else:
					old_red += 20
			else:
				if old_red - 20 < new_red:
					old_red = new_red
				else:
					old_red -= 20

		if old_green != new_green:
			if old_green < new_green:
				if old_green + 20 > new_green:
					old_green = new_green
				else:
					old_green += 20
			else:
				if old_green - 20 < new_green:
					old_green = new_green
				else:
					old_green -= 20

		if old_blue != new_blue:
			if old_blue < new_blue:
				if old_blue + 20 > new_blue:
					old_blue = new_blue
				else:
					old_blue += 20
			else:
				if old_blue - 20 < new_blue:
					old_blue = new_blue
				else:
					old_blue -= 20

		data['args'] = ',red_energy=' + str(old_red) + ',green_energy=' + str(old_green)+ ',blue_energy=' + str(old_blue)
		print(data['args'])
		if old_red == new_red and old_blue == new_blue and old_green == new_green:
			break;

	array_of_RGB_values.append([new_red, new_green, new_blue])
