import requests

url = 'https://www.vrbo.com/graphql'

headers = {
    'authority': 'www.vrbo.com',
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'client-info': 'shopping-pwa,unknown,unknown',
    'content-type': 'application/json',
    'origin': 'https://www.vrbo.com',
    'cookie': "linfo=v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1; CRQS=t|9001`s|9001001`l|en_US`c|USD; currency=USD; tpid=v.1,9001; hav=cdd7ef2c-5c31-7956-0389-a6fb945956d2; MC1=GUID=cdd7ef2c5c3179560389a6fb945956d2; DUAID=cdd7ef2c-5c31-7956-0389-a6fb945956d2; ha-device-id=cdd7ef2c-5c31-7956-0389-a6fb945956d2; hav=cdd7ef2c-5c31-7956-0389-a6fb945956d2; _gcl_au=1.1.1693190545.1700249663; _fbp=fb.1.1700249663535.870324860; OptanonAlertBoxClosed=2023-11-17T19:34:26.064Z; OIP=ccpa|1`ts|1700249666; xdid=6ab89a26-43ba-4abe-b40d-048ecc2327fd|1700249669|vrbo.com; s_fid=751AD26A46D5C75E-1D9662A9A4513BE6; QSI_SI_aWQdMdC3KF1RI10_intercept=true; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Nov+20+2023+13%3A52%3A18+GMT%2B0530+(India+Standard+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=927ee8bc-c315-4ab4-8926-05e0060b66c1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=IN%3BCH&AwaitingReconsent=false; aspp=v.1,0|||||||||||||; _ga=GA1.2.1924316392.1700475768; CRQSS=e|1; iEAPID=1; s_ppv=%5B%5BB%5D%5D; s_ips=1; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; session_id=be574450-6755-4919-9774-8963c07c98fd; page_name=page.Hotel-Search; _cls_v=34d5d705-8236-4e0d-bd5b-fd906e9a8ce9; _cls_s=c4b069db-f0a5-4303-a94d-b85e32df2a46:0; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C19694%7CMCMID%7C18439981346053663073455550440919209970%7CMCAAMLH-1702107270%7C12%7CMCAAMB-1702107270%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1701509670s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; __gads=ID=e893818b40669bb9:T=1700249662:RT=1701502491:S=ALNI_MYBch3iFHD3WBdtTQpgQXfEfXtG5Q; __gpi=UID=00000c8cc3054387:T=1700249662:RT=1701502491:S=ALNI_MYAz_nduave3aeFIKks5SuuWmfuDQ; JSESSIONID=03C3366B8CD932A9CBE13339BEE9D996; _uetvid=4f0e6080858011ee8278fbd5e694b689; HMS=1bb04f22-f8a8-4867-9934-b9cd69e19b7c; has=187a9507-5d39-223c-8d87-7de76a43054e; ak_bmsc=D80F275E0FE3E70B6C8FCC18FEBD19F6~000000000000000000000000000000~YAAQiLYRYDWJ7jCMAQAA6g28PhbYhUvqvK7nXJM6oUv19P5eENDcVOYuQBLoLxf+VZHqSDENBiFCZ37vkRGIVnrWHSurxSUXSeCvE8+/ernstToE1ClIlbzD4anTZp9eJjZm6oTDfACE5Hz6QAobJIclmBjPUbTN5TuHn7SHthFYma1HT6O+QmlTyexoRu1b4i+L38PtOBGE2AyfXyKFekVJ2mVyerIZkV4b2lcEy738U3BzB4gtwbL2sT1TAODbxASN7mHA25MBU8epAMPTuSU/8Ta2B3EPTCzTpelcL2xvM7NnlTOb/Ae0+kgv3o3u0df/zspR5SD2rIYFvqYY7+oR4mAlu2y1chlhJG816sFCe22WkXDvRqpTNGxEPHAE1QNzYMHJtg==; s_ppn=page.Hotel-Search; _tq_id.TV-8181636390-1.1968=7a4c790888da3d81.1700249664.0.1701859972..; QSI_HistorySession=https%3A%2F%2Fwww.vrbo.com%2Fsearch%3Fadults%3D2%26amenities%3D%26children%3D%26d1%3D2023-11-19%26d2%3D2023-11-20%26destination%3DDowntown%2520Chicago%252C%2520Chicago%252C%2520Illinois%252C%2520United%2520States%2520of%2520America%26endDate%3D2023-12-15%26latLong%3D%26mapBounds%3D%26pwaDialog%3D%26regionId%3D6350699%26semdtl%3D%26sort%3DRECOMMENDED%26startDate%3D2023-12-14%26theme%3D%26userIntent%3D~1701859972300; cesc=%7B%22lpe%22%3A%5B%22b4b81f11-ce28-4457-b482-71bf1868483d%22%2C1701860471598%5D%2C%22marketingClick%22%3A%5B%22false%22%2C1701860471598%5D%2C%22lmc%22%3A%5B%22DIRECT.REFERRAL%22%2C1701860471598%5D%2C%22hitNumber%22%3A%5B%224%22%2C1701860471597%5D%2C%22amc%22%3A%5B%22DIRECT.REFERRAL%22%2C1701860471598%5D%2C%22visitNumber%22%3A%5B%2223%22%2C1701859967709%5D%2C%22ape%22%3A%5B%22fdbb7fa4-db90-4dbc-bf6a-d80100016c38%22%2C1701860471598%5D%2C%22entryPage%22%3A%5B%22page.Hotel-Search%22%2C1701860471597%5D%2C%22cid%22%3A%5B%22Brand.DTI%22%2C1700249651848%5D%7D; bm_sv=677AE19556F953ACC7BB4A9289FA1C7E~YAAQBKgRYP2lLBqMAQAAAvbJPhZn/Vd3UK1yzMKmRgMqO75A4UzdsKK68rZn2vtVyAthElLtDZiClqyCUefnWAFYJxcFj3Z/xIppSgbH3RnUqHYoPChyHez1/RL/xUGsG9xVZZPnsU2AjVGNsvfWfOzqKJYAKsliOELWNkxo2oiCXorJyfNQz1iQsDV1DPf0bXQzvnpiO1TYlL1ABKE1TIv1VcdISxXInrzVSQJ9ZWmM4HlGwe4l2THmH8+3yS8=~1; _dd_s=rum=0&expire=1701861383508; s_tp=2442",  # Replace with your actual cookie data
    'referer': 'https://www.vrbo.com/search?adults=2&amenities=&children=&d1=2023-11-19&d2=2023-11-20&destination=Downtown+Chicago%2C+Chicago%2C+Illinois%2C+United+States+of+America&endDate=2023-12-15&latLong=&mapBounds=&pwaDialog=&regionId=6350699&semdtl=&sort=RECOMMENDED&startDate=2023-12-14&theme=&userIntent=',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-enable-apq': 'true',
    'x-page-id': 'page.Hotel-Search,H,20',
}

payload = {
    "variables": {
        "context": {
            "siteId": 9001001,
            "locale": "en_US",
            "eapid": 1,
            "currency": "USD",
            "device": {"type": "DESKTOP"},
            "identity": {"duaid": "cdd7ef2c-5c31-7956-0389-a6fb945956d2", "expUserId": None, "tuid": None,
                         "authState": "ANONYMOUS"},
            "privacyTrackingState": "CAN_TRACK",
            "debugContext": {"abacusOverrides": []}
        },
        "criteria": {
            "primary": {
                "dateRange": {
                    "checkInDate": {"day": 14, "month": 12, "year": 2023},
                    "checkOutDate": {"day": 15, "month": 12, "year": 2023}
                },
                "destination": {
                    "regionName": "Downtown Chicago, Chicago, Illinois, United States of America",
                    "regionId": "6350699",
                    "coordinates": None,
                    "pinnedPropertyId": None,
                    "propertyIds": None,
                    "mapBounds": None
                },
                "rooms": [{"adults": 2, "children": []}]
            },
            "secondary": {
                "counts": [{"id": "resultsStartingIndex", "value": 50}, {"id": "resultsSize", "value": 50}],
                "booleans": [],
                "selections": [
                    {"id": "sort", "value": "RECOMMENDED"},
                    {"id": "privacyTrackingState", "value": "CAN_TRACK"},
                    {"id": "useRewards", "value": "SHOP_WITHOUT_POINTS"},
                    {"id": "searchId", "value": "09bdcdfa-b7d8-4061-9fcf-1bb71a8605ee"}
                ],
                "ranges": []
            }
        },
        "destination": {
            "regionName": None,
            "regionId": None,
            # Add other destination details if needed
        },
        "shoppingContext": {"multiItem": None},
        "returnPropertyType": False,
        "includeDynamicMap": True
    },
    "operationName": "LodgingPwaPropertySearch",
    "extensions": {
        "persistedQuery": {"sha256Hash": "5247eef59f2303d0d40b7ca21bf547835e8bfb321b26ca802a58c2f4a78697c3", "version": 1}
    }
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
