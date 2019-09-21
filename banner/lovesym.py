def symbol():
    print('''
    
                                                                              
                             ████▒                                    
                             █  ▒█░                            ▒██ ▓█▒
                             █   ▒█  ███    ███   █▓██         ███████
                             █    █ ▓▓ ▒█  ▓▓ ▒█  █▓ ▓█        ███████
                             █    █ █   █  █   █  █   █        ▒██████
                             █    █ █████  █████  █   █         █████ 
                             █   ▒█ █      █      █   █          ███  
                             █  ▒█░ ▓▓  █  ▓▓  █  █▓ ▓█           █░  
                             ████▒   ███▒   ███▒  █▓██                
                                                  █                   
                                                  █                   
                                                  █                   
                                

    ''')


def row():
    print('''
╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸╺━╸
    ''')


def yname():
    your_name = input('''        
╻ ╻┏━┓╻ ╻┏━┓   ┏┓╻┏━┓┏┳┓┏━╸    
┗┳┛┃ ┃┃ ┃┣┳┛   ┃┗┫┣━┫┃┃┃┣╸    ╹
 ╹ ┗━┛┗━┛╹┗╸   ╹ ╹╹ ╹╹ ╹┗━╸   ╹   ''')
    len_your_name = len(your_name)
    if len_your_name == 0:
        print("[-] Umm! I think you forgot to enter your name. \n [*] Please Enter Your Name.")
        return yname()
    return your_name


def lname():
    lover_name = input('''         
╻ ╻┏━┓╻ ╻┏━┓   ╻  ┏━┓╻ ╻┏━╸┏━┓╻┏━┓   ┏┓╻┏━┓┏┳┓┏━╸       
┗┳┛┃ ┃┃ ┃┣┳┛   ┃  ┃ ┃┃┏┛┣╸ ┣┳┛ ┗━┓   ┃┗┫┣━┫┃┃┃┣╸    ╹   
 ╹ ┗━┛┗━┛╹┗╸   ┗━╸┗━┛┗┛ ┗━╸╹┗╸ ┗━┛   ╹ ╹╹ ╹╹ ╹┗━╸   ╹   ''')
    len_lover_name = len(lover_name)
    if len_lover_name == 0:
        print("[-] Umm! I think you forgot to enter your lover's name. \n [*] Please Enter Your Lover's Name")
        return lname()
    return lover_name
