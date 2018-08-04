
import html2text
import urllib.request

while True:
    whatYear = input('\nEnter Year:\n')
    if int(whatYear) not in range(1700, 2101):
        print("\nPlease enter a year between 1700 and 2100.")
    else:
        whatMonth = input('\nEnter Month (1 - 12 i.e. July would be 7):\n')
        whatDay = input('\nEnter day of the month:\n')
        whatCity = input('\nEnter City:\n')
        whatCity = whatCity.replace(" ", "+")
        state = input('\nEnter State: (i.e. NM for New Mexico)\n')
        whatState = state.upper()
        site = f'http://aa.usno.navy.mil/cgi-bin/aa_altazw.pl?form=1&body=10&year={whatYear}&month={whatMonth}' \
               f'&day={whatDay}&intv_mag=1&state={whatState}&place={whatCity}'
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27' \
                            ' Safari/537.17'
        req = urllib.request.Request(site, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        string = respData.decode('utf-8')
        text = html2text.html2text(str(respData))

        for row in text:
            time = row

        if int(whatYear) not in range(1700, 2101):
            print("Please enter a year between 1700 and 2100.")

        else:
            below = string.find(' 30.')
            if ' 30.' not in string:
                print("\nSun angle does not reach 30 degrees on this day and at this location.\n")
            else:
                print("\n30 degree sun angle is at:\n\n", string[below - 11:below - 6], "in the morning")
                eveningtime = string.rfind((' 30.'))
                print("", string[eveningtime - 11:eveningtime - 6], "in the evening.")




















