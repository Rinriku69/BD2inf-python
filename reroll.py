import pyautogui # type: ignore
import time
import pydirectinput # type: ignore
import keyboard # type: ignore
import winsound # type: ignore

# Character File Name (INPUT)
TARGET_CHAR_IMAGE1 = "character/helena2.png" 
TARGET_CHAR_IMAGE2 = "character/levia1.png" 

# Position For Star (INPUT)
SLOT_TOP_Y_STARS = 653
SLOT_BOTTOM_Y_STARS = 674 
FIRST_SLOT_LEFT_X_STARS = 370
SLOT_WIDTH_STARS = 95

# Slot Space (INPUT)
SLOT_SPACING = 25 

# Character Image (INPUT)
TARGET_CHAR_SLOT_TOP_Y = 398
TARGET_CHAR_SLOT_BOTTOM_Y = 656 
TARGET_CHAR_FIRST_SLOT_LEFT_X = 371
TARGET_CHAR_SLOT_WIDTH = 98

# Button Position (INPUT)
DRAW_AGAIN_X, DRAW_AGAIN_Y = 1462, 999
SKIP_X, SKIP_Y = 1765, 59

# Hotkey (INPUT)
SCRIPT_TOGGLE_KEY = 'f9'
SCRIPT_QUIT_KEY = 'esc'

# -------SETTING--------------------

# Condition
REQUIRED_5_STAR_COUNT = 3

# Delays
DELAY_AFTER_CLICK = 0.5
DELAY_AFTER_PULL_SEQUENCE = 0.5 
DELAY_BETWEEN_SLOT_CHECKS = 0.02
DELAY_BEFORE_RETRY = 0.2

# Image search confidence (0.0 to 1.0, higher is stricter)
FIVE_STAR_CONFIDENCE = 0.8 
TARGET_CHAR_CONFIDENCE = 0.8 

# -----------------------------------

#Script State
script_active = False
keep_script_running = True


# 5 star image
FIVE_STAR_IMAGE = "star/fivestar.png"
NUMBER_OF_SLOTS_TO_CHECK = 10



#-------- Script State Functions ---------
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
#
#--------------------------------------

#Hotkey register
try:
    keyboard.add_hotkey(SCRIPT_TOGGLE_KEY, toggle_script_state) # to start/stop
    keyboard.add_hotkey(SCRIPT_QUIT_KEY, quit_script)      # to quit the script entirely
    print(f"Script loaded. Press {SCRIPT_TOGGLE_KEY.upper()} to Start/Stop. Press {SCRIPT_QUIT_KEY.upper()} to Exit.")
except Exception as e:
    print(f"Failed to register hotkeys. Try running the script as an administrator. Error: {e}")
    print("Exiting script.")
    exit()



# ****** DEBUG ZONE 🛠️ **********

#Debug for buttons position
'''pyautogui.click(DRAW_AGAIN_X, DRAW_AGAIN_Y)
time.sleep(DELAY_AFTER_CLICK)
pyautogui.press('enter')
time.sleep(DELAY_AFTER_CLICK)

for y in range(10): 
    pyautogui.click(SKIP_X, SKIP_Y)
    time.sleep(0.2) '''

#Debug for specific slot
""" slot_to_check = 9
current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (slot_to_check * (SLOT_WIDTH_STARS + SLOT_SPACING))
star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)
location = pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region)

if location:
     print(f"Found 5-star at {location}")
     pyautogui.click(pyautogui.center(location)) 
else:
     print("5-star not found in this slot.") """

#Debug for search loop
'''found_5_star_count = 0
target_character_found_this_pull = False

for i in range(NUMBER_OF_SLOTS_TO_CHECK):
    current_slot_num = i + 1
    
    # Search for Star----------
    current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
    star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)

    try:
        if pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region):
            found_5_star_count += 1
            print(f"Found 5-star: at {current_slot_num}")
            print(f"Currently 5-star found: {found_5_star_count}")
    except Exception as e: 
        
        print(f"Error searching for 5-star: {e} at slot {current_slot_num}")
        print(f"Currently 5-star found: {found_5_star_count}") 
   #----------------------------

   # Search For Target Character
    current_slot_x_target = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
    target_search_region = (current_slot_x_target, TARGET_CHAR_SLOT_TOP_Y, TARGET_CHAR_SLOT_WIDTH, TARGET_CHAR_SLOT_BOTTOM_Y - TARGET_CHAR_SLOT_TOP_Y)

    if not target_character_found_this_pull:
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE1, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull = True
        except Exception as e:
            p = e
            print(f"Error searching for target character: {e} at slot {current_slot_num}")

    time.sleep(DELAY_BETWEEN_SLOT_CHECKS)
   #----------------------------
print(f"This pull: 5-Stars found: {found_5_star_count}, Target Character found: {target_character_found_this_pull}")'''
#
# **********************************


#Main Function
try:
 total_pull = 0
 while keep_script_running:
  # Draw again and skip-------------------------
  if script_active: 
    pyautogui.click(DRAW_AGAIN_X, DRAW_AGAIN_Y)
    time.sleep(DELAY_AFTER_CLICK)
    pydirectinput.press('enter')    
    time.sleep(DELAY_AFTER_CLICK)
    for y in range(4): 
      pyautogui.click(SKIP_X, SKIP_Y)
      time.sleep(0.2)
    time.sleep(DELAY_AFTER_PULL_SEQUENCE)
  #---------------------------------------------
  
    target_character_found_this_pull1 = False
    target_character_found_this_pull2 = False
    found_5_star_count = 0
    
    # ------[][][][][] Loop for Search on each slot [][][][][]---------

    for i in range(NUMBER_OF_SLOTS_TO_CHECK):
     if not script_active: break 
     current_slot_num = i + 1
     
     #==========  5  STAR SEARCH =========================
     
     #Find Star Area Position
        # --Find most left position of star
     current_slot_x_stars = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
        # --Find star area
     star_search_region = (current_slot_x_stars, SLOT_TOP_Y_STARS, SLOT_WIDTH_STARS, SLOT_BOTTOM_Y_STARS - SLOT_TOP_Y_STARS)
     #--------------------------------

    # Check if 5 star found in current slot
     try:
         if pyautogui.locateOnScreen(FIVE_STAR_IMAGE, confidence=FIVE_STAR_CONFIDENCE, region=star_search_region):
            found_5_star_count += 1
            #print(f"5 Star Found at SLOT #{current_slot_num}")
     except Exception as e: 
        pass
    #-------------------------------------
    
    #====================================================
    
    
    #============ TARGET CHARACTER SEARCH =====================
    
    #Find Target Character Image Area Position
        # --Find most left on X Axis
     current_slot_x_target = FIRST_SLOT_LEFT_X_STARS + (i * (SLOT_WIDTH_STARS + SLOT_SPACING))
        # --Find image position
     target_search_region = (current_slot_x_target, TARGET_CHAR_SLOT_TOP_Y, TARGET_CHAR_SLOT_WIDTH, TARGET_CHAR_SLOT_BOTTOM_Y - TARGET_CHAR_SLOT_TOP_Y)
    #--------------------------------
    
    # Check if target was already found
     if not target_character_found_this_pull1:
         # Check if image pixel match with the target
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE1, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull1 = True
        except Exception as e:
            pass

     if not target_character_found_this_pull2:
        try:
            if pyautogui.locateOnScreen(TARGET_CHAR_IMAGE2, confidence=TARGET_CHAR_CONFIDENCE, region=target_search_region):
                target_character_found_this_pull2 = True
        except Exception as e:
            pass

    #-----STOP CONDITION-------
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




