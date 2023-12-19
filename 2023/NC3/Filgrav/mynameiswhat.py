import csv
import pandas as pd

#The idea is to check all renaming of all files in chronological order

#path to parsed jfile (csv output from mftecmd)
jpath="./filer/j.csv/joutput.csv"
df= pd.read_csv(jpath)

#get all entry ID's
entries=df["EntryNumber"].unique()

#select each entry 
for entry in entries:
    #Only select "renameOldName" and RenameNewName"
    renamed=df.loc[(df['EntryNumber'] == entry) & ((df['UpdateReasons'] == "RenameOldName") | (df['UpdateReasons'] == "RenameNewName"))]
    #Only get entries that actually have been renamed
    if not renamed.empty:
        #Make sure the entries have the same parent entry (in the same dir)
        parents=renamed["ParentEntryNumber"].unique()
        for parent in parents:
            prename=renamed.loc[(df['ParentEntryNumber'] == parent)] 
            #get only the name
            rows=prename[["Name"]]
            total=''
            prev=''
            #Now loop and concant the renames
            for index,row in rows.iterrows():
                current=row["Name"]
                if not current == prev:
                    prev=current
                    total+=current+" -> "
            total=total[:-4]
            print(total)