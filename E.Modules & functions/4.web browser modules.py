"""web browser
# webbrowser - Interfaces for launching and remotely controlling Web browsers.
# It allows the system to launch the default web browser /or installed web broswer to particular url which is typed in
# py file.
# it open the url to default browser if launched with www or http/https but withou both like google.com then it launches
# IE (internet explorer for that url.
"""
import webbrowser
"""
in unix based system which do not have graphical browser then the text based browser but when it called/opened then it 
blocks the further code/process until the browser closed.. like below only first open will run , further one will not.
"""
# open(url,new=0,autoraise=True)
# webbrowser.open('http://www.fb.com/', new=1, autoraise=True)
# here new =1 open the url in new window of browser if possible. it might not gave effect on chrome,firefox instead it
# open the new tab in same browser window.
# webbrowser.open('http://www.fb.com/',new=2,autoraise=False)   # this will open the new browser page("tab").
# webbrowser.open('google.com') # opens the IE not default browser.
webbrowser.open("https://www.python.org/")
########################################################################################################################

# open_new(url) # it need only one param and launch url in new window of browser if possible.
webbrowser.open_new('https://www.gmail.com/')
########################################################################################################################

# open_new_tab(url) # it open the new page("tab") in the browser if possible. otherwise equivalent to open_new().
webbrowser.open_new_tab('https://www.yahoo.com/')
########################################################################################################################

# webbrowser.get(using=none) # return a controller object for specified browser type
# it helps us to launch url in our defined url if we dont want it to launch by default url
mozilla = webbrowser.get('windows-default')
mozilla.open('www.google.com')
#######################################################################################################################

