"""
A module with a single function that downloads the nasdaqtraded.txt file
 and pulls out the ticker symbols and re-writes them to a file.  Each symbol
 will be written to a new line.

The web page to go to:
ftp://ftp.nasdaqtrader.com/SymbolDirectory/
File used: nasdaqtraded.txt
"""
from datetime import datetime
import os
#Change if desired.
download_to_filepath = '/tmp'
#Enter the filepath to the saved nasdaqtraded.txt fileself.
nasdaqlisted_file = '{}/nasdaqtraded.txt'.format(download_to_filepath)
#Add current date to saved stock list
today = datetime.now().strftime('%Y-%m-%d')
#Replace as needed.
save_to_filepath = '/home/user/Desktop/stock_list_{}.txt'.format(today)


def nasdaq_ftp_sorter(download_to_filepath, nasdaqlisted_file,
    save_to_filepath):
    #Automatically get nasdaq traded and save to download_to_filepath directory
    #This invokes bash or sh wget command
    #Will do anytime this script is run and add new file.
    #If using tmp, it cleans itself
    #regularly enough that I'm not concerned.
    #You could add at end of script to delete it:
    #os.system('rm {}/nasdaqtraded.txt'.format(download_to_filepath))
    #Warning, rm is powerfull and if wrong will delete important files!!
    os.system(
        'wget -P {} ftp://ftp.nasdaqtrader.com/SymbolDirectory/'
        'nasdaqtraded.txt'.format(download_to_filepath)
        )
    sym_list = []
    counter = 0
    #Open nasdaqtraded.txt file.
    #Sort out all the symbols from ordinary stocks/shares.
    with open(nasdaqlisted_file, 'r') as f:
        for each in f:
            counter += 1
            split = each.split('|')
            ticker = split[1]
            name = split[2]
            #Junking class shares, going to lose some data
            #if you wanted A and B shares.
            #Honestly the only one I can think of that I care about is BRK-A/B
            #If you care, fix example:
            #if '$A' in str(ticker):
            #    sym_list.append(ticker.replace('$', '-'))
            #Appends list with STOCK-A
            if '$' in str(ticker) or '.' in str(ticker):
                continue
            #Nasdaq has a bunch of test symbols, junking those.
            #Also, added .lower() to string, missed this earlier and it matters.
            if 'test' in str(name.lower()):
                continue
            elif 'stock' in str(name.lower()):
                sym_list.append(ticker)
            elif 'ordinary shares' in str(name.lower()):
                sym_list.append(ticker)
            elif 'common shares' in str(name.lower()):
                sym_list.append(ticker)
            else:
                pass
    #Saving symbols to file.
    for each in sym_list:
        with open(save_to_filepath, 'a+') as file:
            file.write('{}\n'.format(each))
    print(
        'We evaluated {} traded nasdaq symbols and saved {} symbols to the'
        ' file after filtering!'.format(counter, len(sym_list)))

if __name__ == '__main__':
    nasdaq_ftp_sorter(
        download_to_filepath, nasdaqlisted_file, save_to_filepath
        )
