# Web Crawler Tool
## Overview

This web crawler uses a word list to find webpages that may have been left exposed by accident to the public. It also gives an idea for the available attack service, possibly exposing hidden webpages. It is useful for finding accidently exposed pages that may contain information or access that you should not have access to.

## How To Use

####

```
When you first run the python script in your terminal it will first ask for a wordlist of your choice. Drag it then and then click enter. Once this has been processed it will then ask for your target URL. Once this has been processed it will then return all the directories within that web site derived from that wordlist. 
```

## Basic Command Usage

#### Command 1
```
requests library - used to establish a connection tot he webpage to get response
multiprocessing.pool, ThreadPool - used to share the wordlist array across all threads
time - Used to time the script to let the user know how long it ran for
```
#### Command 2
```
ThreadPool from the multiprocessing.pool library - used to share the wordlist array across all threads
```


#### Command 3
```
time library - Used to time the script to let the user know how long it ran for
```

## Open Issues

#### Issue 1

```
The main issue with this tool is the it only goes one directory deep which only allows a small amount of information to be shown. This is something that can be improved in future iterations.
```

#### Issue 2


```
Multithreading has caused some of the words in the wordlist to be skipped - removing multithreading will resolve this issue however it will slow it down drastically
```