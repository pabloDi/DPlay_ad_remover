#GRUIDE: https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

from selenium import webdriver
import time


#Starts the driver
#Opens Dplay
#Presents welcome meny

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.dplay.no")
    inp = ""
    while inp != "0":
        welcomeMeny()
        inp = input()
        checkInput(inp, driver)

    try:
        driver.close()
    except:
        print("Browser window already closed")

#Presents the user with alternatives
def welcomeMeny():
    alternatives = {0: "Exit", 1: "Fjern Reklame"}
    print("Velg hva du vil gjøre!:")
    for alt in alternatives:
        print(str(alt) + " : " + str(alternatives[alt]))



#Checks which input you've given
def checkInput(inp, driver):
    if inp == str(1):
        adBlock(driver)

#Removes the ads
def adBlock(driver):
    try:
        element = driver.find_element_by_id("adsbase")
        attr = element.get_attribute("src")
    except:
        print("No advertisement to remove\n")
        return
    newUrl = checkURL(attr)
    if newUrl:
        driver.execute_script("document.getElementById('adsbase').setAttribute('src', '')", element)
        #Should find a better soluton than sleep (i think)
        time.sleep(0.5)
        adBlock(driver)
    else:
        print("No advertisement to remove\n")


def checkURL(url):
    #Wack måte å gjøre det på, bruk regex eller noe annet
    if url[0:17] == "https://www.dplay":
        print(url[0:17])
        return False
    elif url == "":
        return False
    else:
        print(url[0:17])
        return True


main()