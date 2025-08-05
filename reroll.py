import pyautogui # type: ignore
import time
import pydirectinput # type: ignore
import keyboard # type: ignore
import winsound # type: ignore

script_active = False
keep_script_running = True


DRAW_AGAIN_X, DRAW_AGAIN_Y = 1462, 999
SKIP_X, SKIP_Y = 1765, 59


FIVE_STAR_IMAGE = "star/fivestar.png"
TARGET_CHAR_IMAGE1 = "character/helena2.png" 
TARGET_CHAR_IMAGE2 = "character/levia1.png" 

# Image search confidence (0.0 to 1.0, higher is stricter)
FIVE_STAR_CONFIDENCE = 0.8 
TARGET_CHAR_CONFIDENCE = 0.8 

REQUIRED_5_STAR_COUNT = 3
NUMBER_OF_SLOTS_TO_CHECK = 10


SLOT_TOP_Y_STARS = 653
SLOT_BOTTOM_Y_STARS = 674 
FIRST_SLOT_LEFT_X_STARS = 370
SLOT_WIDTH_STARS = 95
SLOT_SPACING = 25 


TARGET_CHAR_SLOT_TOP_Y = 398
TARGET_CHAR_SLOT_BOTTOM_Y = 656 
TARGET_CHAR_FIRST_SLOT_LEFT_X = 371
TARGET_CHAR_SLOT_WIDTH = 98


# Delays
DELAY_AFTER_CLICK = 0.5
DELAY_AFTER_PULL_SEQUENCE = 0.5 
DELAY_BETWEEN_SLOT_CHECKS = 0.05 
DELAY_BEFORE_RETRY = 0.7

def toggle_script_state():
    global script_active
    script_active = not script_active
    if script_active:
        print("--- Script ACTIVATED by Hotkey ---")
    else:
        print("--- Script DEACTIVATED by Hotkey Current Total pulls ---")

def quit_script():
    global keep_script_running, script_active
    print("--- EXIT Hotkey pressed. Stopping script... ---")
    script_active = False 
    keep_script_running = False 

#Hotkey register
try:
    keyboard.add_hotkey('f9', toggle_script_state) # F9 to start/stop
    keyboard.add_hotkey('esc', quit_script)      # Esc to quit the script entirely
    print("Script loaded. Press F9 to Start/Stop. Press Esc to Exit.")
except Exception as e:
    print(f"Failed to register hotkeys. Try running the script as an administrator. Error: {e}")
    print("Exiting script.")
    exit()


'''pyautogui.click(DRAW_AGAIN_X, DRAW_AGAIN_Y)
time.sleep(DELAY_AFTER_CLICK)
pyautogui.press('enter')
time.sleep(DELAY_AFTER_CLICK)

for y in range(10): 
    pyautogui.click(SKIP_X, SKIP_Y)
    time.sleep(0.2) '''

#Debug for specific slot
'''current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (9 * (SLOT_WIDTH_STARS + SLOT_SPACING))
star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)
location = pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region)

if location:
     print(f"Found 5-star at {location}")
     pyautogui.click(pyautogui.center(location)) 
else:
     print("5-star not found in this slot.")'''




#Debug for search loop
'''found_5_star_count = 0
target_character_found_this_pull = False

for i in range(NUMBER_OF_SLOTS_TO_CHECK):
    current_slot_num = i + 1
    current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
    
    star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)

    try:
        if pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region):
            found_5_star_count += 1
            #print(f"Found 5-star: at {current_slot_num}")
            #print(f"Currently 5-star found: {found_5_star_count}")
    except Exception as e: 
        
        print(f"Error searching for 5-star: {e} at slot {current_slot_num}")
        #print(f"Currently 5-star found: {found_5_star_count}") 
   



    
    current_slot_x_target = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
    
    target_search_region = (current_slot_x_target, TARGET_CHAR_SLOT_TOP_Y, TARGET_CHAR_SLOT_WIDTH, TARGET_CHAR_SLOT_BOTTOM_Y - TARGET_CHAR_SLOT_TOP_Y)

    if not target_character_found_this_pull:
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE1, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull = True
        except Exception as e:
            p = e
            print(f"Error searching for target character: {e} at slot {current_slot_num}")

    #time.sleep(DELAY_BETWEEN_SLOT_CHECKS)

print(f"This pull: 5-Stars found: {found_5_star_count}, Target Character found: {target_character_found_this_pull}")'''

#main function
try:
 total_pull = 0
 while keep_script_running:
  if script_active: 
    pyautogui.click(DRAW_AGAIN_X, DRAW_AGAIN_Y)
    time.sleep(DELAY_AFTER_CLICK)
    pydirectinput.press('enter')    
    time.sleep(DELAY_AFTER_CLICK)
    for y in range(4): 
      pyautogui.click(SKIP_X, SKIP_Y)
      time.sleep(0.2)
    time.sleep(DELAY_AFTER_PULL_SEQUENCE)
 
    #image search loop
    target_character_found_this_pull1 = False
    target_character_found_this_pull2 = False
    found_5_star_count = 0
    for i in range(NUMBER_OF_SLOTS_TO_CHECK):
     if not script_active: break 

     current_slot_num = i + 1
     current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
     star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)

     try:
         if pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region):
            found_5_star_count += 1
     except Exception as e: 
        print(f"Error searching for 5-star: {e} at slot {current_slot_num}")
    
     current_slot_x_target = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
     target_search_region = (current_slot_x_target, TARGET_CHAR_SLOT_TOP_Y, TARGET_CHAR_SLOT_WIDTH, TARGET_CHAR_SLOT_BOTTOM_Y - TARGET_CHAR_SLOT_TOP_Y)

     if not target_character_found_this_pull1:
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE1, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull1 = True
        except Exception as e:
            print(f"Error searching for target character1: {TARGET_CHAR_IMAGE1} at slot {current_slot_num}")

     if not target_character_found_this_pull2:
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE2, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull2 = True
        except Exception as e:
            print(f"Error searching for target character2: {TARGET_CHAR_IMAGE2} at slot {current_slot_num}")

    #stop condition
    if (found_5_star_count>=REQUIRED_5_STAR_COUNT) :
         total_pull = total_pull + 10
         print(f"Success! Found {found_5_star_count} 5-star with total {total_pull} pulls! Stopping script. Press Esc to Exit.")
         script_active = False 
         sound_file = "star/tuturu.wav"
         try:
          winsound.PlaySound(sound_file, winsound.SND_FILENAME)
         except Exception as e_sound:
          print(f"Error playing sound: {e_sound},{sound_file}")
          winsound.Beep(1000, 500)
    else:
         total_pull = total_pull + 10
         print(f"Conditions not met, re-pulling after a delay... current total pulls {total_pull}")
         time.sleep(DELAY_BEFORE_RETRY)
  else:
    time.sleep(0.1) 

except KeyboardInterrupt: 
    print("\n--- Script interrupted by user (Ctrl+C). Exiting. ---")

finally:
    print("--- Cleaning up hotkeys... ---")
    keyboard.unhook_all_hotkeys() 
    print("--- Script fully exited. ---")




