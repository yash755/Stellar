import requests
import json
import csv

cursor = 0

while True:

    try:

        url = "https://api.stellar.expert/explorer/public/asset/XLM/holders"

        querystring = {"cursor": str(cursor),"filter":"asset-holders","limit":"50","order":"asc","tag[]":"personal"}

        headers = {
            'sec-ch-ua': "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            'sec-ch-ua-mobile': "?0",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            'accept': "*/*",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'cache-control': "no-cache",
            'postman-token': "8441c0e4-4e3e-1a3d-123f-6c6d97606fb0"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        if '_embedded' in data:
            embedded = data['_embedded']
            if 'records' in embedded:
                records = embedded['records']

                if len(records) >= 1:
                    for record in records:

                        rank = ''
                        account = ''

                        if 'position' in record:
                            rank = record['position']

                        if 'account' in record:
                            account = record['account']


                        if account:

                            temp = []
                            temp.append(rank)
                            temp.append(account)

                            print(temp)

                            arr = []
                            arr.append(temp)

                            with open('main.csv', 'a+') as csvfile:
                                csvwriter = csv.writer(csvfile)

                                # writing the data rows
                                csvwriter.writerows(arr)


                else:
                    break


        cursor = cursor + 49

    except:
        continue



