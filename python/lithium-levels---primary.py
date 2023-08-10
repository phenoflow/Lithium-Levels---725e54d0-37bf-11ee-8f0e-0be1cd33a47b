# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"44W8.00","system":"readv2"},{"code":"44W8100","system":"readv2"},{"code":"44W8200","system":"readv2"},{"code":"46P3.00","system":"readv2"},{"code":"6657.11","system":"readv2"},{"code":"6657.12","system":"readv2"},{"code":"665B.00","system":"readv2"},{"code":"9859","system":"oxmis"},{"code":"L 130L","system":"oxmis"},{"code":"L 130L9","system":"oxmis"},{"code":"L 130LA","system":"oxmis"},{"code":"L 130LB","system":"oxmis"},{"code":"L 130LC","system":"oxmis"},{"code":"L 130LD","system":"oxmis"},{"code":"T3551CA","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lithium-levels-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lithium-levels---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lithium-levels---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lithium-levels---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
