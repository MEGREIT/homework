kutxe = input("Chawere romeli kutxidan xar: ")



def qartveloba(kutxe):
    Kaxeli = {
    "your spirit animal": "Viri",
    "your favorite food": "xinkali",
    "your favorite activity": "rtveli",
    "your favorite swear word": "mogian jigari",
    "your dogs name": "mura",
    "most basic male name in your family tree": "alika",
    "most basic female name in your family tree":"lamara or jujuna",
    "your favorite drink": "wine",
    "your favorite fruit": "grapes",
    "your favorite snack": "sazamtros muraba"

}
    
    Mtiuli = {
    "your spirit animal": "Cxvari",
    "your favorite food": "xinkali",
    "your favorite activity": "nadiroba",
    "your favorite swear word": "every single one.",
    "your dogs name": "loma",
    "most basic male name in your family tree": "all names are popular there",
    "most basic female name in your family tree": "same as males",
    "your favorite drink": "xlebnaia vodka",
    "your favorite fruit": "qliavi",
    "your favorite snack": "gudis yveli",
            
}
    if kutxe == "kaxeti":
        for key, value in Kaxeli.items():
            print(key, value)
    if kutxe == "mtiuleti":
        return(Mtiuli)
    else:
        return("debili xoar xar dzma")
    

qartveloba(kutxe=kutxe)
