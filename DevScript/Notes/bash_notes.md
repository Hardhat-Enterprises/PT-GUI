# Bash Quickstart Guide

Extracted from bash tutorial located [here](https://www.youtube.com/watch?v=e7BufAVwDiM).

---

## BASICS

#### Shows all available shells
```bash
cat /etc/shells
```

#### Show path of bash
```bash
which bash
output is generally /bin/bash
```

#### First line
```bash
#! /bin/bash
```

#### Print out cmd
```bash
echo
```

#### Operators
```bash
-lt less than
-le less than equals to
-gt greater than
-ge greater than equals to
-eq equals
```
---

## REDIRECTING TO FILES

#### Save to file
```bash
echo "text here" > filename.txt
```

#### User input outputs to file
```bash
cat > filename.txt
```
After running the script the user can write what they want in the terminal and it will be available in filename.txt

#### User input appends to file.
```bash
cat >> filename.txt
```
Adds the text to the end of the file instead of replacing it all together.

---

## COMMENTING

#### One line comments
```bash
#your comment here
```

#### Multiple line comments
```bash
: '
comment
comment
comment '
```

#### Output comments to terminal
```bash
cat << variablename
comment
comment
variablename
```

---

## CONDITIONAL STATEMENTS

#### IF statements
Note: if statements brackets must always have a space on the left and right . -eq is equals (=) . -gt is greater than (>).
```bash
count=10
if [ $count -eq 10 ]
then
	echo "the condition is true"
else
	echo "the condition is false"
fi

if [ $count -gt 9 ]
then
	echo "the condition is true"
else
	echo "the condition is false"
fi
```

Note: if you want to use symbols such as > or < you change the if statement to be in the syntax below
the spaces are also necessary in between the brackets and the condition.
```bash
if (( $count < 9 ))
then
	echo "true"
fi
```

#### Using AND
```bash
age=10

if [ "$age" -gt 18 ] && [ "$age" -lt 40 ]
then
	echo "Age is correct"
else
	echo "Age is not correct"
fi
```

#### Using OR
```bash
age=10

if [ "$age" -gt 18 ] || [ "$age" -lt 40 ]
then
	echo "Age is correct"
else
	echo "Age is not correct"
fi
```

#### Using case
```bash
car=$1
case $car in
	"BMW" )
		echo "It's BMW" ;;
	"Mercedes" )
		echo "It's Mercedes" ;;
	"Toyota" )
		echo "It's Toyota" ;;
	"Honda" )
		echo "It's Honda" ;;
		* )
		echo "unknown car name" ;;
	esac
```
---

## LOOPS

#### While loops
Note: runs until the condition is true.
```bash
number=1
while [ $number -lt 10 ]
do
	echo "$number"
	number=$(( number+1 ))
done
```

#### Until loops
Note: runs until the condition BECOMES true.
```bash
number=1
until [ $number -ge 10 ]
do
	echo "$number"
	number=$(( number+1 ))
done
```

#### For loops
Note: this will print out numbers 1 2 3 4 5.
```bash
for i in 1 2 3 4 5         
do
	echo $i
done
```
Note: this will print out numbers 1 - 20.
```bash
for i in {0..20}           
do
	echo $i
done
```
Note: this will print out 1 - 20 incrementing by 2, e.g. 0,2,4,6,8..20.
```bash
for i in {0..20..2}
do
	echo $i
done
```       

#### i++ for loop
```bash
for (( i=0; i<5 i++ ))
do
	echo $i
done
```

#### Loops with conditions
Note: if $i is greater than 5 the loop will return a break.
```bash
for (( i=0; i<=10 i++ ))
do
	if [$i -gt 5]
		then
			break
	fi
	echo $i
done
```

#### Continue statement in loop
Note: execute everything except for if the number is 3 or 7. (these numbers wont be printed).
```bash
for (( i=0; i<=10 i++ ))
do
	if [$i -eq 3] || [ $i -eq 7]
		then
			continue
	fi
	echo $i
done
```
---

## SCRIPT INPUT - STDIN

#### Arguments
```bash
echo $1 $2 $3
```
This allows you to set the arguments $1 $2 $3 whilst executing the script: `./script.sh Argument1 Argument2 Argument3`

`$0` will output the script name as its the first argument.

#### Arguments in arrays
```bash
args=("$@")

echo ${args[0]} ${args[1]} ${args[2]}
```
Note: this will print out specific arrays: `./script 0thArrayIndex 1stArrayIndex 2ndArrayIndex`

```bash
echo $@
```
Note: this will print out all arrays e.g. ./script array1 array2 array3 array4 ..

```bash
echo $#
```
Note: print out the length of the array.

#### Reading a file with STDIN
```bash
while read line
do
	echo "$line"
done < "${1:-/dev/stdin}"  
```
	./script document\ name\ 1
	Note: the slashes are used to tell the input that it is 1 file. The slashes represent the spaces for a file titled "document name 1".

---

## SCRIPT OUTPUT - STOUT AND STDERR
#### Standard Output
```bash
	ls -al 1>file1.txt 2>file2.txt
```
Note: this will output an ls on the current directory to file1.txt. Any errors that the terminal returns will be in file2.txt. This can be useful for printing out results from enumeration.
