"""
A module with a single function that takes the nasdaqtraded.txt downloaded file
 and pulls out the ticker symbols and re-writes them to a file.  Each symbol
 will be written to a new line.

The web page to go to:
ftp://ftp.nasdaqtrader.com/SymbolDirectory/
Now download nasdaqtraded.txt
"""

#Enter the filepath to the saved nasdaqtraded.txt fileself.
#example: '/home/user/Desktop/nasdaqtraded.txt'
nasdaqlisted_filepath = ''
#Enter the file name as a filepath, with file name and extension.
#example: '/home/user/Desktop/ticker_list.txt'
save_to_filepath = ''

def nasdaq_ftp_sorter(nasdaqlisted_filepath, save_to_filepath):
    file = open(nasdaqlisted_filepath)
    new_stock_list = []
    counter = 0
    for each in file:
        counter +=1
        #Drop first two characters of line.
        cut = each[2:]
        #Stop reading line at |.
        end = cut.find("|")
        #Result is the stock symbol.
        ticker = cut[:end]
        #Then we take everything after stock symbol and |.
        next = each[(2+len(ticker)+1):]
        #Now we're cutting off the end so the ticker description remains.
        next_end = next.find("|")
        #Finally, all that remains is ticker description.
        pnext = next[:next_end]
        #Filtering out actual stocks, no etfs, class shares, ect.
        if pnext[-5:] == 'Stock':
            new_stock_list.append(ticker)
        elif pnext[-15:] == 'Ordinary Shares':
            new_stock_list.append(ticker)
        elif pnext[-13:] == 'Common Shares':
            new_stock_list.append(ticker)
    for each in new_stock_list:
        #cleaning out the strange symbols, and different share classes
        if '$' not in each and '.' not in each:
            #appending it to a file
            with open('{}'.format(save_to_filepath), 'a+') as file:
                file.write('{}\n'.format(each))
    print('We evaluated {} traded nasdaq symbols and saved {} symbols to the'
          ' file after filtering!'.format(counter, len(new_stock_list)))

#If you don't know what this does, it's unlikely you'll be able to use this.
if __name__ == '__main__':
    nasdaq_ftp_sorter(nasdaqlisted_filepath, save_to_filepath)
