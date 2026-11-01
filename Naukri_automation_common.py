{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from selenium import webdriver\
from selenium.webdriver.common.by import By\
from selenium.webdriver.common.keys import Keys\
from webdriver_manager.chrome import ChromeDriverManager\
from selenium.webdriver.chrome.service import Service\
from selenium.webdriver.support.ui import WebDriverWait\
from selenium.webdriver.support import expected_conditions as EC\
from datetime import datetime\
\
def log(message):\
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")\
    print(f"[\{timestamp\}] \{message\}", flush=True)\
    \
import time\
\
# Launch browser\
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))\
driver.get("https://www.naukri.com/")\
driver.maximize_window()\
\
time.sleep(1)\
\
# Click Login button\
login_btn = driver.find_element(By.XPATH, "//a[text()='Login']")\
login_btn.click()\
\
time.sleep(1)\
\
# Enter Email\
email_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")\
email_box.send_keys(\'93your@email.id)\
\
# Enter Password\
password_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")\
password_box.send_keys(\'93your password)\
\
# Click Login submit\
submit_btn = driver.find_element(By.XPATH, "//button[text()='Login']")\
submit_btn.click()\
\
print("-------------START---------------------")\
\
log("Logged In")\
\
\
# Go to profile\
time.sleep(1)\
\
# Go directly to profile page\
driver.get("https://www.naukri.com/mnjuser/profile")\
\
#time.sleep(5)\
log("Viewed Profile")\
\
wait = WebDriverWait(driver, 20)\
resume_headline = wait.until(\
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Resume headline')]"))\
)\
\
# CLICK EDIT ICON (PENCIL)\
edit_icon = driver.find_element(\
    By.XPATH,\
    "//span[contains(text(),'Resume headline')]/ancestor::div[contains(@class,'widgetHead')]//span[contains(@class,'edit')]"\
)\
driver.execute_script("arguments[0].click();", edit_icon)\
\
log("Clicked Edit")\
time.sleep(3)\
log("Edited")\
\
\
# Locate textarea\
headline_box = driver.find_element(By.TAG_NAME, "textarea")\
\
current_text = headline_box.get_attribute("value")\
\
# Add dot\
headline_box.clear()\
headline_box.send_keys(current_text + ".")\
\
log("Added Dot text")\
\
# Save\
save_btn = driver.find_element(By.XPATH, "//button[text()='Save']")\
save_btn.click()\
\
\
log("Saved")\
\
time.sleep(3)\
\
# ---- Remove dot ----\
#edit_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Resume headline')]/ancestor::div[contains(@class,'widgetHead')]//span[contains(@class,'edit')]")\
#edit_btn.click()\
\
# Click edit again\
edit_icon = wait.until(EC.element_to_be_clickable(\
    (By.XPATH, "//span[contains(text(),'Resume headline')]/ancestor::div[contains(@class,'widgetHead')]//span[contains(@class,'edit')]")\
))\
driver.execute_script("arguments[0].click();", edit_icon)\
\
log("Editing again to remove dot")\
\
# Wait for textarea\
headline_box = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))\
\
# Get current text\
current_text = headline_box.get_attribute("value")\
\
# Remove dot if present\
updated_text = current_text.rstrip(".")\
\
# Update field\
headline_box.clear()\
headline_box.send_keys(updated_text)\
\
# Save again\
save_btn = driver.find_element(By.XPATH, "//button[text()='Save']")\
save_btn.click()\
\
log("Removed dot and saved")\
\
time.sleep(3)\
\
current_time = datetime.now().strftime("%d %B %Y | %I:%M:%S %p")\
\
driver.execute_script(f"""\
var box = document.createElement('div');\
\
box.innerHTML = "\uc0\u10004  Profile Updated Today<br><br>\{current_time\}";\
\
box.style.position = "fixed";\
box.style.top = "50%";\
box.style.left = "50%";\
box.style.transform = "translate(-50%, -50%)";\
\
box.style.width = "6in";\
box.style.height = "2in";\
\
box.style.backgroundColor = "#d4edda";\
box.style.border = "2px solid #28a745";\
box.style.borderRadius = "12px";\
\
box.style.display = "flex";\
box.style.flexDirection = "column";\
box.style.alignItems = "center";\
box.style.justifyContent = "center";\
\
box.style.fontSize = "28px";\
box.style.fontWeight = "bold";\
box.style.color = "#155724";\
box.style.textAlign = "center";\
\
box.style.boxShadow = "0 8px 25px rgba(0,0,0,0.3)";\
box.style.zIndex = "9999";\
\
document.body.appendChild(box);\
\
setTimeout(function()\{\{\
    box.remove();\
\}\}, 5000);\
""")\
\
\
\
log("Updated Today")\
print("Done for Today!")\
print("-------------END---------------------")\
time.sleep(2)\
\
driver.quit()\
}