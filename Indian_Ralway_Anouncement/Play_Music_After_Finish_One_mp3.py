import os
import pygame
import time

def play_mp3(file_path):
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Load and play the mp3 file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():
    # Print greeting message
    print("!! Jai Shree Ram !!")
    
    # Get the current directory and list files
    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)
    
    # Filter mp3 files
    mp3_files = [f for f in file_list if os.path.splitext(f)[1] == '.mp3']
    
    # Sort the files if needed (e.g., by name)
    mp3_files.sort()
    
    # Play each mp3 file one by one
    for mp3_file in mp3_files:
        print(f"Playing: {mp3_file}")
        play_mp3(mp3_file)
    
if __name__ == '__main__':
    main()
