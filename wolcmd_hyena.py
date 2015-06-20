#Created by Kin-Ho Lam 6/19/15 for the COF Helpdesk
import sys, os, datetime

def create_old_wol():	#moves wolcmd.dat to Old WOL and renames it to wolcmd[YYYY-MM-DD].dat
	wolcmd = "\\\\pteridium\\Groups\\FCR\\hyena\\wolcmd.dat";	#location of wolcmd.dat if it exists
	old_wol = "\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL";	#location of Old WOL directory if it exists
	wolcmd_date = "\\\\pteridium\\Groups\\FCR\\hyena\\Old WOL\wolcmd" + str(datetime.date.today()) + ".dat";	#location of wolcmd[today's date].dat
	if(os.path.exists(wolcmd)):	#checks if wolcmd.dat exists, if not exit function
		if not (os.path.exists(old_wol)):	#checks if Old WOL directory exists, if not creates Old WOL directory
			os.mkdir(old_wol);
		if (os.path.exists(wolcmd_date)):	#overwrite if there exists a .dat log with the same date
			os.remove(wolcmd_date);
		os.rename(wolcmd, wolcmd_date);	#renames and moves wolcmd.dat

def create_wol(): #creates wolcmd.dat
	zone_path = "\\\\staticweb\\zoneinfo\\zone.txt";	#address of zone.txt
	wolcmd_path = "\\\\pteridium\\Groups\\FCR\\hyena\\wolcmd.dat";	#address of wolcmd.dat
	if(os.path.exists(zone_path)):	#checks if zone.txt exists, if not end the script
		zone = open(zone_path, 'r');	#opens zone.txt
	else:
		return; #exit the program if there is no zone.txt
	wolcmd = open(wolcmd_path, 'w+'); #opens or creates wolcmd.dat
	for line in zone: #loop for every line in zone.txt
		entry = line.split(",'"); #deliminates line every ,'
		wolcmd.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "")); #removes ', .fsl.orst.edu, .cof.orst.edu, and .forestry.oregonstate.edu from name
		wolcmd.write('\t');	#tab
		mac_addr = '-'.join(entry[2][i:i+2] for i in range(0, len(entry[2]), 2)); #adds a - every two letters in the mac address
		wolcmd.write(mac_addr.replace("-'", "")); #removes the -' at the end because it adds one every two letters
		wolcmd.write('\n'); #new line
	zone.close();	#closes zone.txt
	wolcmd.close();	#closes wolcmd.dat
	#entry[0] = machine name , entry[2] = Mac address
	
def main(): #main
	create_old_wol();
	create_wol();
	
main(); #run main
