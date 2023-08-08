# Collect number of hits(h),at bats(ab),validate data,calculate batting average(ba),display

check=0

while check < 1:
	h=input("Enter the player's number of hits: ")
	ab=input("Enter the player's times at bat: ")

	if (h.isdigit()) and (ab.isdigit())and (int(ab) >= int(h)):
		ba="{:.3f}".format(int(h)/int(ab))
		print("\n\n\tA player with",h,"hits and",ab,"at bats would have a batting average of",ba,"\n\n\n")
		check=1
	else:	
		print("Please enter valid values for hits and at bats.\n\n")
