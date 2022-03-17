# -*- coding: utf-8 -*-
import requests
from multiprocessing.pool import ThreadPool
import time

#import wordlist as a list so it can be split for each thread
file = open(input("Drag in wordlist: ").strip("'"),"r")
lines = file.read().split('\n')


found_urls=[] 

#main functions that the threads are each runngin for their selected words
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

#Variables set for the target and the timer
target_url = input("[*] Enter The Target URL: ")
print("Scanning...")
start_time = time.process_time()

#Count to determine the amout of pages it has checked 
searched = 0 

#Main function that is called by the threads 
def main(lines):
    global searched
    word = lines.strip()
    full_url = target_url + "/" + word
    response = request(full_url)
    if response:
        print("[+] Directory found " + full_url)
        found_urls.append(full_url)
    else: 
        print("[-] Directory not found " + full_url)
    searched += 1
         
#Opens all threads and assigns them the main function
pool = ThreadPool()
pool.map(main, lines)
pool.join

#Prints the finished message with # of words searched and a total time
print("Searched", searched, "pages in",(time.process_time()-start_time),"seconds!")