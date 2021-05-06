# Get-Similar-Files
## A simple python script to get top 5 visible similar files for your query<br>

Usage -
In your current folder
python3 path_to_FuzzSearch.py 

#### For using install fuzzywuzzy and python-Levenshtein python packages. 

#### Uses fuzz partial ratio from fuzzywuzzy. <br>
#### It uses edit distance to get the similarity ratio and return its maximum in any substring of the two
#### queried strings.<br>

#### Can also use from terminal with a bash function like -
```
Search(){
     python3 path_to_file $@
}
```
#### and then 
```
Search some_file
```
#### Put up the function in some bash file .Custom.sh and put that file path under ~/.bashrc as -
```
source ~/.Custom.sh
```
#### and then use it whenever you want