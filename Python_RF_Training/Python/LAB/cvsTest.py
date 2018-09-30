#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     19/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tablib
import os
def main():
    CURR_DIR = os.path.dirname(__file__)

    # create a dataset
    data = tablib.Dataset()

    # Add rows
    data.append(["A", 1])
    data.append(["B", 2])
    data.append(["C", 3])

    # save as csv
    with open(os.path.join(CURR_DIR, 'test.csv'), 'wb') as f:
        f.write(data.csv)

    # save as Excel
    with open(os.path.join(CURR_DIR,'test.xls'), 'wb') as f:
        f.write(data.xls)

    # save as Excel 07+
    with open(os.path.join(CURR_DIR,'test.xlsx'), 'wb') as f:
        f.write(data.xlsx)
if __name__ == '__main__':
    main()
