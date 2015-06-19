#Created by Kin-Ho Lam 6/19/15 for the COF Helpdesk
import sys, os, datetime

def create_old_wol():	#moves wolcmd.dat to Old WOL and renames it to wolcmd[YYYY-MM-DD].dat
	if(os.path.exists("\\\\pteridium\\Groups\\FCR\\hyena\\wolcmd.dat")):	#checks if wolcmd.dat exists, if not exit function
		if not (os.path.exists("\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL")):	#checks if Old WOL directory exists, if not creates Old WOL directory
			os.mkdir("\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL");
		if (os.path.exists( "\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL\wolcmd" + str(datetime.date.today()) + ".dat")): #overwrite if there exists a .dat log with the same name
			os.remove("\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL\wolcmd" + str(datetime.date.today()) + ".dat");

		os.rename("\\\\pteridium\\Groups\\FCR\\hyena\\wolcmd.dat", "\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL\wolcmd" + str(datetime.date.today()) + ".dat");	#renames and moves wolcmd.dat

def create_wol(): #creates wolcmd.dat
	zone_path = "\\\\staticweb\\zoneinfo\\zone.txt";	#address of zone.txt
	wolcmd_path = "\\\\pteridium\\Groups\\FCR\\hyena\\wolcmd.dat"; #address of wolcmd.dat

	if(os.path.exists(zone_path)):	#checks if zone.txt exists, if not end the script
		zone = open(zone_path, 'r'); #opens zone.txt
	else:
		return; #exit the program if there is no zone.txt

	wolcmd = open(wolcmd_path, 'w+'); #opens or creates wolcmd.dat
	for line in zone: #loop for every line in zone.txt
		spot = line.split(",'"); #deliminates line every ,'
		wolcmd.write(spot[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "")); #removes ', .fsl.orst.edu, .cof.orst.edu, and .forestry.oregonstate.edu from name
		wolcmd.write('\t');	#moves to a new line after each entry
		mac_addr = '-'.join(spot[2][i:i+2] for i in range(0, len(spot[2]), 2)); #adds a - every two letters in the mac address
		wolcmd.write(mac_addr.replace("-'", "")); #removes the -' at the end because it adds one every two letters
		wolcmd.write('\n'); #new line

	zone.close();	#closes zone.txt
	wolcmd.close();	#closes wolcmd.dat
	#spot[0] = machine name , spot[2] = Mac address
	
def main(): #main
	create_old_wol();
	create_wol();
	
main(); #run main
