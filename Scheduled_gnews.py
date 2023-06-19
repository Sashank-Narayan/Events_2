{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aw3t3CeVN9NW",
        "outputId": "302677d7-7388-45fc-8948-16a219e876a1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting GoogleNews\n",
            "  Downloading GoogleNews-1.6.8-py3-none-any.whl (8.1 kB)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from GoogleNews) (4.11.2)\n",
            "Collecting dateparser (from GoogleNews)\n",
            "  Downloading dateparser-1.1.8-py2.py3-none-any.whl (293 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m293.8/293.8 kB\u001b[0m \u001b[31m7.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from GoogleNews) (2.8.2)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->GoogleNews) (2.4.1)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.10/dist-packages (from dateparser->GoogleNews) (2022.7.1)\n",
            "Requirement already satisfied: regex!=2019.02.19,!=2021.8.27 in /usr/local/lib/python3.10/dist-packages (from dateparser->GoogleNews) (2022.10.31)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.10/dist-packages (from dateparser->GoogleNews) (4.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->GoogleNews) (1.16.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal->dateparser->GoogleNews) (0.1.0.post0)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal->dateparser->GoogleNews) (2023.3)\n",
            "Installing collected packages: dateparser, GoogleNews\n",
            "Successfully installed GoogleNews-1.6.8 dateparser-1.1.8\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting gnewsclient\n",
            "  Downloading gnewsclient-1.12-py3-none-any.whl (7.9 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from gnewsclient) (2.27.1)\n",
            "Collecting fuzzywuzzy (from gnewsclient)\n",
            "  Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)\n",
            "Collecting feedparser (from gnewsclient)\n",
            "  Downloading feedparser-6.0.10-py3-none-any.whl (81 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m81.1/81.1 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting sgmllib3k (from feedparser->gnewsclient)\n",
            "  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->gnewsclient) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->gnewsclient) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->gnewsclient) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->gnewsclient) (3.4)\n",
            "Building wheels for collected packages: sgmllib3k\n",
            "  Building wheel for sgmllib3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6046 sha256=f00a5a4bbee0156ffad3a1e586af0a91b2270eb070c4670e3641612e884fb6d9\n",
            "  Stored in directory: /root/.cache/pip/wheels/f0/69/93/a47e9d621be168e9e33c7ce60524393c0b92ae83cf6c6e89c5\n",
            "Successfully built sgmllib3k\n",
            "Installing collected packages: sgmllib3k, fuzzywuzzy, feedparser, gnewsclient\n",
            "Successfully installed feedparser-6.0.10 fuzzywuzzy-0.18.0 gnewsclient-1.12 sgmllib3k-1.0.0\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting snscrape==0.6.2.20230320\n",
            "  Downloading snscrape-0.6.2.20230320-py3-none-any.whl (71 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m71.8/71.8 kB\u001b[0m \u001b[31m3.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: requests[socks] in /usr/local/lib/python3.10/dist-packages (from snscrape==0.6.2.20230320) (2.27.1)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.10/dist-packages (from snscrape==0.6.2.20230320) (4.9.2)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from snscrape==0.6.2.20230320) (4.11.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from snscrape==0.6.2.20230320) (3.12.0)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->snscrape==0.6.2.20230320) (2.4.1)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->snscrape==0.6.2.20230320) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->snscrape==0.6.2.20230320) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->snscrape==0.6.2.20230320) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->snscrape==0.6.2.20230320) (3.4)\n",
            "Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from requests[socks]->snscrape==0.6.2.20230320) (1.7.1)\n",
            "Installing collected packages: snscrape\n",
            "Successfully installed snscrape-0.6.2.20230320\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting rake_nltk\n",
            "  Downloading rake_nltk-1.0.6-py3-none-any.whl (9.1 kB)\n",
            "Requirement already satisfied: nltk<4.0.0,>=3.6.2 in /usr/local/lib/python3.10/dist-packages (from rake_nltk) (3.8.1)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.10/dist-packages (from nltk<4.0.0,>=3.6.2->rake_nltk) (8.1.3)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.10/dist-packages (from nltk<4.0.0,>=3.6.2->rake_nltk) (1.2.0)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/dist-packages (from nltk<4.0.0,>=3.6.2->rake_nltk) (2022.10.31)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from nltk<4.0.0,>=3.6.2->rake_nltk) (4.65.0)\n",
            "Installing collected packages: rake_nltk\n",
            "Successfully installed rake_nltk-1.0.6\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/fuzzywuzzy/fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning\n",
            "  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')\n"
          ]
        }
      ],
      "source": [
        "!pip install GoogleNews\n",
        "!pip install gnewsclient\n",
        "!pip install snscrape==0.6.2.20230320\n",
        "!pip install rake_nltk\n",
        "\n",
        "import pandas as pd\n",
        "# from newsapi import NewsApiClient\n",
        "import requests\n",
        "from GoogleNews import GoogleNews\n",
        "from gnewsclient import gnewsclient\n",
        "import snscrape.modules.twitter as sntwitter\n",
        "from datetime import datetime, date\n",
        "import json\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import nltk\n",
        "from nltk.tokenize import sent_tokenize, word_tokenize\n",
        "from nltk.corpus import stopwords\n",
        "from string import punctuation\n",
        "import re\n",
        "import numpy as np\n",
        "from nltk.tokenize import RegexpTokenizer\n",
        "from nltk.stem import WordNetLemmatizer\n",
        "from rake_nltk import Rake\n",
        "from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "id425SVcN9Nb"
      },
      "outputs": [],
      "source": [
        "start_date = []\n",
        "end_date = []"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9z79OMANN9Nc"
      },
      "outputs": [],
      "source": [
        "sources = [\"bbc-news\", \"the-telegraph\", \"the-guardian-uk\", \"cnn\", \"abc-news-au\",\n",
        "           \"dailymail.co.uk\", \"metro.co.uk\", \"mirror.co.uk\", \"news.google.com\"]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "bgr77j2AN9Nd"
      },
      "outputs": [],
      "source": [
        "all_keywords = ['strike', 'holiday', 'lockdown',\n",
        "            'inflation', 'grocery sales', 'carnival', 'festival', 'party', 'Walmart', \"Tesco\", \"Sainsbury's\", \"supply chain\", \"flood\", \"wendys\", \"lidl\"]\n",
        "\n",
        "# all_keywords = ['tesco', 'holiday']\n",
        "\n",
        "# all_keywords = ['autumn', 'bank']\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Pqjh5tBuy7hC"
      },
      "outputs": [],
      "source": [
        "keywords = ['Lidl','Tesco','Walmart','Sainsbury\\'s', 'Aldi', 'Asda', 'Marks & Spencers', 'Morrison\\'s']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "98VGmhUlrzSq"
      },
      "outputs": [],
      "source": [
        "events = ['autumn bank holiday']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UlDJce6V8jka"
      },
      "outputs": [],
      "source": [
        "all_events = ['autumn bank holiday']\n",
        "\n",
        "final_prod_events = pd.DataFrame()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cKZSWp8ZWckH"
      },
      "outputs": [],
      "source": [
        "counter = 6000"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Etrp7MlCN9Ne"
      },
      "outputs": [],
      "source": [
        "gnews_client_topics = ['Top Stories',\n",
        "                       'World',\n",
        "                       'Nation',\n",
        "                       'Business',\n",
        "                       'Technology',\n",
        "                       'Entertainment',\n",
        "                       'Sports',\n",
        "                       'Science',\n",
        "                       'Health']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aiYeWUcQUhqR"
      },
      "outputs": [],
      "source": [
        "# branch_keyword_bu_num = {'Esher' : 1, 'Dorchester' : 2}\n",
        "branch_keyword_bu_num = {\n",
        "'Peterborough': 103,\n",
        "'Gillingham': 105,\n",
        "'Dorking': 107,\n",
        "'St Ives': 108,\n",
        "'Brighton': 114,\n",
        "'Brent Cross': 119,\n",
        "'Dorchester': 120,\n",
        "'Esher': 121,\n",
        "'Hall Green': 122,\n",
        "'Whetstone': 124,\n",
        "'Coulsdon': 129,\n",
        "'New Malden': 131,\n",
        "'Allington Park': 137,\n",
        "'Bury St Edmunds': 140,\n",
        "'Blaby': 141,\n",
        "'Marlow': 146,\n",
        "'Kingsthorpe': 148,\n",
        "'East Sheen': 149,\n",
        "'Four Oaks': 150,\n",
        "'Westbury Park': 151,\n",
        "'Leighton Buzzard': 154,\n",
        "'Stourbridge': 155,\n",
        "'Bromley': 158,\n",
        "'Birch Hill': 159,\n",
        "'Ramsgate': 160,\n",
        "'Huntingdon': 163,\n",
        "'Marlborough': 164,\n",
        "'Green Street Green': 165,\n",
        "'St Albans': 166,\n",
        "'Stevenage': 167,\n",
        "'Havant': 171,\n",
        "'John Barnes': 174,\n",
        "'Hertford': 175,\n",
        "'Beaconsfield': 177,\n",
        "'Enfield': 179,\n",
        "'Goldsworth Park': 181,\n",
        "'Sevenoaks': 182,\n",
        "'St Neots': 185,\n",
        "'Ruislip': 197,\n",
        "'Banstead': 202,\n",
        "'Ringwood': 203,\n",
        "'Welwyn Garden City': 204,\n",
        "'Ely': 205,\n",
        "'Thame': 206,\n",
        "'Chichester': 208,\n",
        "'Southend': 213,\n",
        "'Henley': 214,\n",
        "'Finchley': 215,\n",
        "'Godalming': 216,\n",
        "'Monmouth': 217,\n",
        "'Reading': 218,\n",
        "'Cirencester': 220,\n",
        "'Berkhamsted': 223,\n",
        "'Putney': 225,\n",
        "'Salisbury': 226,\n",
        "'Billericay': 229,\n",
        "'Horley': 233,\n",
        "'Okehampton': 234,\n",
        "'Waterlooville': 239,\n",
        "'Biggin Hill': 240,\n",
        "'Banstead': 324,\n",
        "'Horsham New': 580,\n",
        "'Heathfield': 595,\n",
        "'Cambridge': 651,\n",
        "'Hailsham': 653,\n",
        "'Hythe': 654,\n",
        "'Paddock Wood': 655,\n",
        "'Saltash': 656,\n",
        "'Sidmouth': 657,\n",
        "'Sudbury': 658,\n",
        "'Thatcham': 659,\n",
        "'Worcester Park': 661,\n",
        "'Wymondham': 662,\n",
        "'Cheltenham': 663,\n",
        "'Belgravia': 665,\n",
        "'Tonbridge': 667,\n",
        "'Chandlers Ford': 668,\n",
        "'Portishead': 669,\n",
        "'Romsey': 671,\n",
        "'Wandsworth': 673,\n",
        "'Newmarket': 674,\n",
        "'Sandbach': 680,\n",
        "'Fulham': 681,\n",
        "'Towcester': 682,\n",
        "'Abergavenny': 683,\n",
        "'Hitchin': 685,\n",
        "'Swaffham': 686,\n",
        "'Newport': 687,\n",
        "'Barry': 688,\n",
        "'Worthing': 689,\n",
        "'Otley': 691,\n",
        "'Farnham': 692,\n",
        "'Dartford': 693,\n",
        "'Sheffield': 695,\n",
        "'Wolverhampton': 696,\n",
        "'Willerby': 697,\n",
        "'Lichfield': 699,\n",
        "'Wilmslow': 711,\n",
        "'Lewes': 727,\n",
        "'East Grinstead': 741,\n",
        "'Buxton': 748,\n",
        "'St Katharine Docks': 753,\n",
        "'West Ealing': 764,\n",
        "'Hersham': 765,\n",
        "'Bishop s Stortford': 101,\n",
        "'Buckhurst Hill': 102,\n",
        "'Epsom': 104,\n",
        "'Longfield': 109,\n",
        "'Crowborough': 110,\n",
        "'Holloway Road': 112,\n",
        "'Milton Keynes': 115,\n",
        "'Dibden': 118,\n",
        "'Burgess Hill': 123,\n",
        "'Temple Fortune': 125,\n",
        "'Saffron Walden': 135,\n",
        "'Evington': 136,\n",
        "'Witney': 142,\n",
        "'Harrow Weald': 143,\n",
        "'Gosport': 152,\n",
        "'Wantage': 153,\n",
        "'Daventry': 156,\n",
        "'Weybridge': 157,\n",
        "'Winton': 161,\n",
        "'Andover': 168,\n",
        "'Southsea': 170,\n",
        "'Kings Road': 173,\n",
        "'Cobham': 176,\n",
        "'Caterham': 178,\n",
        "'Woodley': 180,\n",
        "'Harpenden': 183,\n",
        "'Caversham': 184,\n",
        "'Northwood': 186,\n",
        "'Richmond': 188,\n",
        "'West Byfleet': 189,\n",
        "'Sunningdale': 190,\n",
        "'Barnet': 191,\n",
        "'Chesham': 192,\n",
        "'Bath': 193,\n",
        "'Maidenhead': 194,\n",
        "'Kingston': 195,\n",
        "'Fleet': 196,\n",
        "'Yateley': 198,\n",
        "'Horsham': 200,\n",
        "'Tenterden': 201,\n",
        "'Bloomsbury': 207,\n",
        "'Petersfield': 209,\n",
        "'Stroud': 210,\n",
        "'Abingdon': 211,\n",
        "'Beckenham': 212,\n",
        "'South Harrow': 219,\n",
        "'Wokingham': 221,\n",
        "'Norwich': 222,\n",
        "'Bromley South': 224,\n",
        "'Newark': 227,\n",
        "'Gloucester Road': 230,\n",
        "'South Woodford': 231,\n",
        "'Surbiton': 232,\n",
        "'Staines': 235,\n",
        "'Marylebone': 236,\n",
        "'Great Malvern': 237,\n",
        "'Twyford': 238,\n",
        "'Byres Road': 308,\n",
        "'Weston Super Mare': 309,\n",
        "'Wellington': 315,\n",
        "'Ashbourne': 316,\n",
        "'Storrington': 317,\n",
        "'Menai Bridge': 318,\n",
        "'Melksham': 319,\n",
        "'Colchester': 455,\n",
        "'JL Foodhall Oxford Street': 456,\n",
        "'Pontprennau': 457,\n",
        "'Crewkerne': 458,\n",
        "'Kenilworth': 460,\n",
        "'Eldon Square': 461,\n",
        "'Westfield London': 462,\n",
        "'Winchester': 463,\n",
        "'Alcester': 474,\n",
        "'Bridport': 475,\n",
        "'Caldicot': 476,\n",
        "'Croydon': 477,\n",
        "'Haslemere': 478,\n",
        "'Headington': 479,\n",
        "'Holsworthy': 480,\n",
        "'Leigh On Sea': 481,\n",
        "'Ponteland': 482,\n",
        "'Saxmundham': 483,\n",
        "'Stamford': 484,\n",
        "'Torquay': 485,\n",
        "'Upminster': 486,\n",
        "'Lutterworth': 487,\n",
        "'Clerkenwell': 492,\n",
        "'JL Foodhall Bluewater': 493,\n",
        "'Altrincham': 494,\n",
        "'Frimley': 652,\n",
        "'Twickenham': 660,\n",
        "'Canary Wharf': 664,\n",
        "'Mill Hill': 670,\n",
        "'Droitwich': 672,\n",
        "'Wallingford': 675,\n",
        "'Newbury': 676,\n",
        "'Sanderstead': 677,\n",
        "'Kensington': 678,\n",
        "'Harrogate': 684,\n",
        "'Rushden': 690,\n",
        "'Lincoln': 694,\n",
        "'Rickmansworth': 698,\n",
        "'Ashford': 705,\n",
        "'Cheadle Hulme': 710,\n",
        "'Balham': 719,\n",
        "'Southampton New': 720,\n",
        "'Ampthill': 722,\n",
        "'Durham': 730,\n",
        "'Barbican': 732,\n",
        "'Formby': 749,\n",
        "'Comely Bank': 750,\n",
        "'Christchurch': 754,\n",
        "'Bayswater': 756,\n",
        "'Eastbourne': 757,\n",
        "'Chiswick': 760,\n",
        "'Morningside': 761,\n",
        "'Parkstone': 766,\n",
        "'Clapham Junction': 767,\n",
        "'Edgware Road': 768,\n",
        "'Buckingham': 769,\n",
        "'Windsor New': 772,\n",
        "'Islington': 780,\n",
        "'Hexham': 782,\n",
        "'Harborne': 796,\n",
        "'Brackley': 797,\n",
        "'Lymington New': 798,\n",
        "'Sandhurst': 799,\n",
        "'Trinity Square': 833,\n",
        "'Clifton': 834,\n",
        "'Crouch End': 835,\n",
        "'Oxted': 838,\n",
        "'Enfield CFC': 199,\n",
        "'Greenford CFC': 259,\n",
        "'Evesham': 303,\n",
        "'York': 311,\n",
        "'Poynton': 312,\n",
        "'East Cowes': 313,\n",
        "'Wimbledon': 314,\n",
        "'Knutsford': 326,\n",
        "'Newton Mearns': 327,\n",
        "'Stratford City': 328,\n",
        "'Alton': 329,\n",
        "'St Saviour (Jersey)': 332,\n",
        "'Rohais (Guernsey)': 333,\n",
        "'St Helier (Jersey)': 334,\n",
        "'Admiral Park (Guernsey)': 335,\n",
        "'Red Houses (Jersey)': 336,\n",
        "'MOUNTSORREL': 403,\n",
        "'Gerrards Cross': 459,\n",
        "'Sevenoaks': 464,\n",
        "'Marlow': 465,\n",
        "'Cardiff Queen Street': 501,\n",
        "'Acton': 502,\n",
        "'Swindon': 504,\n",
        "'Littlehampton': 505,\n",
        "'Uckfield': 506,\n",
        "'Hereford': 507,\n",
        "'Malmesbury': 511,\n",
        "'Coulsdon DFC': 513,\n",
        "'Bagshot': 514,\n",
        "'Nailsea': 515,\n",
        "'Parsons Green': 516,\n",
        "'Egham': 519,\n",
        "'Jesmond': 520,\n",
        "'Enfield Chase': 521,\n",
        "'Sutton Coldfield': 522,\n",
        "'Chippenham': 523,\n",
        "'West Hampstead': 524,\n",
        "'Shrewsbury': 525,\n",
        "'Tottenham Court Road': 526,\n",
        "'Dorking': 527,\n",
        "'Wimbledon Hill': 528,\n",
        "'Hawkhurst': 529,\n",
        "'Fulham Palace Road': 530,\n",
        "'Peterborough': 531,\n",
        "'Canterbury': 533,\n",
        "'Sceptre (Watford)': 534,\n",
        "'Kensington Gardens': 535,\n",
        "'Camden': 536,\n",
        "'Addlestone': 542,\n",
        "'Fitzroy Street': 552,\n",
        "'Teignmouth': 554,\n",
        "'Hornchurch': 555,\n",
        "'Edenbridge': 556,\n",
        "'Keynsham': 557,\n",
        "'Spinningfields': 558,\n",
        "'Cheam': 559,\n",
        "'Alderley Edge': 560,\n",
        "'Walton-on-Thames': 562,\n",
        "'Locks Heath': 563,\n",
        "'Burgh Heath': 567,\n",
        "'Petts Wood': 568,\n",
        "'Portman Square': 569,\n",
        "'Burnt Common': 571,\n",
        "'Walbrook': 573,\n",
        "'Leeds': 574,\n",
        "'Broxbourne': 575,\n",
        "'Amersham': 578,\n",
        "'Bayswater Temp': 579,\n",
        "'Oxford Botley Road': 581,\n",
        "'BASINGSTOKE': 582,\n",
        "'Old Brompton Road': 583,\n",
        "'Hazlemere': 584,\n",
        "'Ealing': 586,\n",
        "'West Kensington': 587,\n",
        "'Palmers Green': 588,\n",
        "'Guildford': 589,\n",
        "'Kings Cross': 590,\n",
        "'Wollaton': 591,\n",
        "'Rustington': 596,\n",
        "'BATTERSEA NINE ELMS': 598,\n",
        "'UTTOXETER': 599,\n",
        "'High Holborn': 601,\n",
        "'Alderley Old': 602,\n",
        "'Sherborne': 604,\n",
        "'Hove': 605,\n",
        "'Leek': 606,\n",
        "'High Wycombe': 607,\n",
        "'Hampton': 612,\n",
        "'Pimlico': 614,\n",
        "'Foregate Street': 615,\n",
        "'Clapham Common': 616,\n",
        "'Kings Cross Station': 619,\n",
        "'Stirling': 620,\n",
        "'North Walsham': 622,\n",
        "'Aylesbury': 625,\n",
        "'Milngavie': 630,\n",
        "'Ipswich': 632,\n",
        "'Manchester Piccadilly': 636,\n",
        "'Highbury Corner': 637,\n",
        "'Muswell Hill': 639,\n",
        "'Knightsbridge': 641,\n",
        "'Solihull': 642,\n",
        "'Sidcup': 643,\n",
        "'Notting Hill Gate': 644,\n",
        "'Truro': 648,\n",
        "'Worcester': 700,\n",
        "'Warminster': 701,\n",
        "'Exeter': 702,\n",
        "'South Bank Tower': 703,\n",
        "'Bracknell': 706,\n",
        "'Stratford Upon Avon': 708,\n",
        "'Walton-le-Dale': 721,\n",
        "'Bedford': 725,\n",
        "'Wootton': 726,\n",
        "'Market Harborough': 728,\n",
        "'Wells': 729,\n",
        "'Poundbury': 733,\n",
        "'Cowbridge': 735,\n",
        "'ROEHAMPTON': 736,\n",
        "'Battersea': 737,\n",
        "'Bagshot Road': 738,\n",
        "'Tubs Hill': 739,\n",
        "'Greenwich': 740,\n",
        "'Colmore Row (Birmingham)': 742,\n",
        "'Ipswich (Corn Exchange)': 743,\n",
        "'Kings Hill': 744,\n",
        "'Chipping Sodbury': 751,\n",
        "'Oakgrove': 752,\n",
        "'Dorking': 755,\n",
        "'Oundle': 758,\n",
        "'Northwich': 759,\n",
        "'Helensburgh': 771,\n",
        "'Monument': 773,\n",
        "'Little Waitrose at John Lewis Watford': 781,\n",
        "'Victoria Street': 783,\n",
        "'Vauxhall': 789,\n",
        "'Horley - Brighton Road': 802,\n",
        "'Wimborne': 805,\n",
        "'Headington - London Road': 806,\n",
        "'Guildford Worplesdon Road': 808,\n",
        "'Little Waitrose John Lewis Southampton': 815,\n",
        "'East Putney': 820,\n",
        "'Meanwood': 828,\n",
        "'Chester': 842,\n",
        "'Raynes Park': 846,\n",
        "'Oadby': 847,\n",
        "'Leatherhead': 859,\n",
        "'Victoria Bressenden Place': 860,\n",
        "'SKY (OSTERLEY)': 865,\n",
        "'Faringdon': 871,\n",
        "'Haywards Heath': 873,\n",
        "'Banbury': 874,\n",
        "'Finchley Central': 876,\n",
        "'Bromsgrove': 877,\n",
        "'Winchmore Hill': 878,\n",
        "}\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MAOuI7dYN9Nf"
      },
      "outputs": [],
      "source": [
        "# England = ['Avon', 'Bedfordshire', 'Berkshire', 'Buckinghamshire', 'Cambridgeshire', 'Cheshire', 'Cleveland',\n",
        "#            'Cornwall', 'Cumbria', 'Derbyshire', 'Devon', 'Dorset', 'Durham', 'East-Sussex', 'Essex', 'Gloucestershire',\n",
        "#            'Hampshire', 'Herefordshire', 'Hertfordshire', 'Isle-of-Wight', 'Kent', 'Lancashire', 'Leice stershire',\n",
        "#            'Lincolnshire', 'London', 'Merseyside',\n",
        "#            'Middlesex', 'Norfolk', 'Northamptonshire', 'Northumberland', 'North-Humberside', 'North-Yorkshire',\n",
        "#            'Nottinghamshire', 'Oxfordshire', 'Rutland', 'Shropshire', 'Somerset', 'South-Humberside', 'South-Yorkshire',\n",
        "#            'Staffordshire', 'Suffolk', 'Surrey', 'Tyne-and-Wear', 'Warwickshire', 'West-Midlands', 'West-Sussex',\n",
        "#            'West-Yorkshire', 'Wiltshire', 'Worcestershire']\n",
        "England = ['London']\n",
        "Wales = ['Clwyd', 'Dyfed', 'Gwent', 'Gwynedd', 'Mid-Glamorgan',\n",
        "         'Powys', 'South-Glamorgan', 'West-Glamorgan']\n",
        "# Wales = ['South-Glamorgan']\n",
        "Scotland = ['Aberdeenshire', 'Angus', 'Argyll', 'Ayrshire', 'Banffshire', 'Berwickshire', 'Bute', 'Caithness',\n",
        "            'Clackmannanshire', 'Dumfriesshire', 'Dunbartonshire', 'East-Lothian', 'Fife', 'Inverness-shire',\n",
        "            'Kincardineshire', 'Kinross-shire',\n",
        "            'Kirkcudbrightshire', 'Lanarkshire', 'Midlothian', 'Moray', 'Nairnshire', 'Orkney', 'Peeblesshire',\n",
        "            'Perthshire', 'Renfrewshire', 'Ross-shire', 'Roxburghshire', 'Selkirkshire', 'Shetland', 'Stirlingshire',\n",
        "            'Sutherland', 'West Lothian', 'Wigtownshire']\n",
        "NorthernIreland = ['Antrim', 'Armagh', 'Down',\n",
        "                   'Fermanagh', 'Londonderry', 'Tyrone']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wqosM5ySN9Ng"
      },
      "outputs": [],
      "source": [
        "# branch_keyword = ['Abergavenny', 'Alderley Edge', \"Eastbourne\", \"Edenbridge\", \"Pontprennau\"]\n",
        "# branch_keyword = ['Abingdon', 'Canary Wharf']\n",
        "# all_branch_keyword = ['Yateley', 'Canary Wharf', 'Workingham', 'Firmley']\n",
        "all_branch_keyword = list(branch_keyword_bu_num.keys())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Q_bhawhRNxnx"
      },
      "outputs": [],
      "source": [
        "branch_keyword = all_branch_keyword"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "bcX9WfgAN9Ng"
      },
      "outputs": [],
      "source": [
        "# countries = [England, Wales, Scotland, NorthernIreland]\n",
        "countries = [England]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yPnMjBxmN9Ng"
      },
      "outputs": [],
      "source": [
        "final = []"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HjbT2oHwGenn"
      },
      "outputs": [],
      "source": [
        "# final_prod = pd.DataFrame()\n",
        "status_val = []"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HlTvy7QmN9Nh"
      },
      "outputs": [],
      "source": [
        "def googleNewsByStreet():\n",
        "    data = pd.DataFrame()\n",
        "    for branch in branch_keyword:\n",
        "        for keyword in keywords:\n",
        "            news = GoogleNews()\n",
        "            news.set_period('1d')\n",
        "            news.get_news(branch + ' ' + keyword)\n",
        "            results = news.result()\n",
        "            df = pd.DataFrame.from_dict(results)\n",
        "            df['keyword'] = keyword\n",
        "            df['branch'] = branch\n",
        "            df['bu_num'] = branch_keyword_bu_num[branch]\n",
        "            print(df)\n",
        "            df.head(5)\n",
        "            data = pd.concat([data, df], ignore_index=True)\n",
        "\n",
        "    # print the dataframe\n",
        "    if len(data.columns) > 4:\n",
        "      data = data.drop(columns=[\"img\", \"site\"])\n",
        "      final.append(data)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kitk6GatN9Nj"
      },
      "outputs": [],
      "source": [
        "def _removeNonAscii(s):\n",
        "    return \"\".join(i for i in s if ord(i) < 128)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1tQpAGeWN9Nj"
      },
      "source": [
        "function to remove the punctuations, apostrophe, special characters using regular expressions"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nQ38jsUDN9Nj"
      },
      "outputs": [],
      "source": [
        "def clean_text(text):\n",
        "    text = text.lower()\n",
        "    text = re.sub(r\"what's\", \"what is \", text)\n",
        "    text = text.replace('(ap)', '')\n",
        "    text = re.sub(r\"\\'s\", \" is \", text)\n",
        "    text = re.sub(r\"\\'ve\", \" have \", text)\n",
        "    text = re.sub(r\"can't\", \"cannot \", text)\n",
        "    text = re.sub(r\"n't\", \" not \", text)\n",
        "    text = re.sub(r\"i'm\", \"i am \", text)\n",
        "    text = re.sub(r\"\\'re\", \" are \", text)\n",
        "    text = re.sub(r\"\\'d\", \" would \", text)\n",
        "    text = re.sub(r\"\\'ll\", \" will \", text)\n",
        "    text = re.sub(r'\\W+', ' ', text)\n",
        "    text = re.sub(r'\\s+', ' ', text)\n",
        "    text = re.sub(r\"\\\\\", \"\", text)\n",
        "    text = re.sub(r\"\\'\", \"\", text)\n",
        "    text = re.sub(r\"\\\"\", \"\", text)\n",
        "    text = re.sub('[^a-zA-Z ?!]+', '', text)\n",
        "    text = _removeNonAscii(text)\n",
        "    text = text.strip()\n",
        "    return text"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4t0WW6sHN9Nj"
      },
      "source": [
        "stop words are the words that convery little to no information about the actual content like the words:the, of, for etc"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZDg2YrQ7N9Nk"
      },
      "outputs": [],
      "source": [
        "def remove_stopwords(word_tokens):\n",
        "    filtered_sentence = []\n",
        "    stop_words = stopwords.words('english')\n",
        "    specific_words_list = ['char', 'u', 'hindustan', 'doj', 'washington']\n",
        "    stop_words.extend(specific_words_list)\n",
        "    for w in word_tokens:\n",
        "        if w not in stop_words:\n",
        "            filtered_sentence.append(w)\n",
        "    return filtered_sentence"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2JJN_S0KN9Nk"
      },
      "source": [
        "function for lemmatization"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "C4HnnrsiN9Nk"
      },
      "outputs": [],
      "source": [
        "def lemmatize(x):\n",
        "    lemmatizer = WordNetLemmatizer()\n",
        "    return ' '.join([lemmatizer.lemmatize(word) for word in x])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nfO_kEyON9Nk"
      },
      "source": [
        "splitting a string, text into a list of tokens"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "n-lwf6tuN9Nk"
      },
      "outputs": [],
      "source": [
        "tokenizer = RegexpTokenizer(r'\\w+')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CASnFpj9N9Nk"
      },
      "outputs": [],
      "source": [
        "def tokenize(x):\n",
        "    return tokenizer.tokenize(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rdQ_hWw_N9Nl",
        "outputId": "0be6d144-ba9c-4c58-9389-96d2a0350165"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading collection 'all'\n",
            "[nltk_data]    | \n",
            "[nltk_data]    | Downloading package abc to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/abc.zip.\n",
            "[nltk_data]    | Downloading package alpino to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/alpino.zip.\n",
            "[nltk_data]    | Downloading package averaged_perceptron_tagger to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping taggers/averaged_perceptron_tagger.zip.\n",
            "[nltk_data]    | Downloading package averaged_perceptron_tagger_ru to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping\n",
            "[nltk_data]    |       taggers/averaged_perceptron_tagger_ru.zip.\n",
            "[nltk_data]    | Downloading package basque_grammars to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping grammars/basque_grammars.zip.\n",
            "[nltk_data]    | Downloading package bcp47 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package biocreative_ppi to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/biocreative_ppi.zip.\n",
            "[nltk_data]    | Downloading package bllip_wsj_no_aux to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping models/bllip_wsj_no_aux.zip.\n",
            "[nltk_data]    | Downloading package book_grammars to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping grammars/book_grammars.zip.\n",
            "[nltk_data]    | Downloading package brown to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/brown.zip.\n",
            "[nltk_data]    | Downloading package brown_tei to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/brown_tei.zip.\n",
            "[nltk_data]    | Downloading package cess_cat to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/cess_cat.zip.\n",
            "[nltk_data]    | Downloading package cess_esp to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/cess_esp.zip.\n",
            "[nltk_data]    | Downloading package chat80 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/chat80.zip.\n",
            "[nltk_data]    | Downloading package city_database to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/city_database.zip.\n",
            "[nltk_data]    | Downloading package cmudict to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/cmudict.zip.\n",
            "[nltk_data]    | Downloading package comparative_sentences to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/comparative_sentences.zip.\n",
            "[nltk_data]    | Downloading package comtrans to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package conll2000 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/conll2000.zip.\n",
            "[nltk_data]    | Downloading package conll2002 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/conll2002.zip.\n",
            "[nltk_data]    | Downloading package conll2007 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package crubadan to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/crubadan.zip.\n",
            "[nltk_data]    | Downloading package dependency_treebank to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/dependency_treebank.zip.\n",
            "[nltk_data]    | Downloading package dolch to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/dolch.zip.\n",
            "[nltk_data]    | Downloading package europarl_raw to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/europarl_raw.zip.\n",
            "[nltk_data]    | Downloading package extended_omw to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    | Downloading package floresta to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/floresta.zip.\n",
            "[nltk_data]    | Downloading package framenet_v15 to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/framenet_v15.zip.\n",
            "[nltk_data]    | Downloading package framenet_v17 to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/framenet_v17.zip.\n",
            "[nltk_data]    | Downloading package gazetteers to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/gazetteers.zip.\n",
            "[nltk_data]    | Downloading package genesis to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/genesis.zip.\n",
            "[nltk_data]    | Downloading package gutenberg to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/gutenberg.zip.\n",
            "[nltk_data]    | Downloading package ieer to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/ieer.zip.\n",
            "[nltk_data]    | Downloading package inaugural to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/inaugural.zip.\n",
            "[nltk_data]    | Downloading package indian to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/indian.zip.\n",
            "[nltk_data]    | Downloading package jeita to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package kimmo to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/kimmo.zip.\n",
            "[nltk_data]    | Downloading package knbc to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package large_grammars to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping grammars/large_grammars.zip.\n",
            "[nltk_data]    | Downloading package lin_thesaurus to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/lin_thesaurus.zip.\n",
            "[nltk_data]    | Downloading package mac_morpho to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/mac_morpho.zip.\n",
            "[nltk_data]    | Downloading package machado to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package masc_tagged to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package maxent_ne_chunker to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping chunkers/maxent_ne_chunker.zip.\n",
            "[nltk_data]    | Downloading package maxent_treebank_pos_tagger to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping taggers/maxent_treebank_pos_tagger.zip.\n",
            "[nltk_data]    | Downloading package moses_sample to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping models/moses_sample.zip.\n",
            "[nltk_data]    | Downloading package movie_reviews to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/movie_reviews.zip.\n",
            "[nltk_data]    | Downloading package mte_teip5 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/mte_teip5.zip.\n",
            "[nltk_data]    | Downloading package mwa_ppdb to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping misc/mwa_ppdb.zip.\n",
            "[nltk_data]    | Downloading package names to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/names.zip.\n",
            "[nltk_data]    | Downloading package nombank.1.0 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package nonbreaking_prefixes to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/nonbreaking_prefixes.zip.\n",
            "[nltk_data]    | Downloading package nps_chat to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/nps_chat.zip.\n",
            "[nltk_data]    | Downloading package omw to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package omw-1.4 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package opinion_lexicon to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/opinion_lexicon.zip.\n",
            "[nltk_data]    | Downloading package panlex_swadesh to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    | Downloading package paradigms to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/paradigms.zip.\n",
            "[nltk_data]    | Downloading package pe08 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/pe08.zip.\n",
            "[nltk_data]    | Downloading package perluniprops to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping misc/perluniprops.zip.\n",
            "[nltk_data]    | Downloading package pil to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/pil.zip.\n",
            "[nltk_data]    | Downloading package pl196x to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/pl196x.zip.\n",
            "[nltk_data]    | Downloading package porter_test to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping stemmers/porter_test.zip.\n",
            "[nltk_data]    | Downloading package ppattach to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/ppattach.zip.\n",
            "[nltk_data]    | Downloading package problem_reports to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/problem_reports.zip.\n",
            "[nltk_data]    | Downloading package product_reviews_1 to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/product_reviews_1.zip.\n",
            "[nltk_data]    | Downloading package product_reviews_2 to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/product_reviews_2.zip.\n",
            "[nltk_data]    | Downloading package propbank to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package pros_cons to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/pros_cons.zip.\n",
            "[nltk_data]    | Downloading package ptb to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/ptb.zip.\n",
            "[nltk_data]    | Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping tokenizers/punkt.zip.\n",
            "[nltk_data]    | Downloading package qc to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/qc.zip.\n",
            "[nltk_data]    | Downloading package reuters to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package rslp to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping stemmers/rslp.zip.\n",
            "[nltk_data]    | Downloading package rte to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/rte.zip.\n",
            "[nltk_data]    | Downloading package sample_grammars to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping grammars/sample_grammars.zip.\n",
            "[nltk_data]    | Downloading package semcor to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package senseval to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/senseval.zip.\n",
            "[nltk_data]    | Downloading package sentence_polarity to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/sentence_polarity.zip.\n",
            "[nltk_data]    | Downloading package sentiwordnet to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/sentiwordnet.zip.\n",
            "[nltk_data]    | Downloading package shakespeare to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/shakespeare.zip.\n",
            "[nltk_data]    | Downloading package sinica_treebank to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/sinica_treebank.zip.\n",
            "[nltk_data]    | Downloading package smultron to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/smultron.zip.\n",
            "[nltk_data]    | Downloading package snowball_data to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    | Downloading package spanish_grammars to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping grammars/spanish_grammars.zip.\n",
            "[nltk_data]    | Downloading package state_union to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/state_union.zip.\n",
            "[nltk_data]    | Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/stopwords.zip.\n",
            "[nltk_data]    | Downloading package subjectivity to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/subjectivity.zip.\n",
            "[nltk_data]    | Downloading package swadesh to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/swadesh.zip.\n",
            "[nltk_data]    | Downloading package switchboard to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/switchboard.zip.\n",
            "[nltk_data]    | Downloading package tagsets to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping help/tagsets.zip.\n",
            "[nltk_data]    | Downloading package timit to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/timit.zip.\n",
            "[nltk_data]    | Downloading package toolbox to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/toolbox.zip.\n",
            "[nltk_data]    | Downloading package treebank to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/treebank.zip.\n",
            "[nltk_data]    | Downloading package twitter_samples to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/twitter_samples.zip.\n",
            "[nltk_data]    | Downloading package udhr to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/udhr.zip.\n",
            "[nltk_data]    | Downloading package udhr2 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/udhr2.zip.\n",
            "[nltk_data]    | Downloading package unicode_samples to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/unicode_samples.zip.\n",
            "[nltk_data]    | Downloading package universal_tagset to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping taggers/universal_tagset.zip.\n",
            "[nltk_data]    | Downloading package universal_treebanks_v20 to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    | Downloading package vader_lexicon to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    | Downloading package verbnet to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/verbnet.zip.\n",
            "[nltk_data]    | Downloading package verbnet3 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/verbnet3.zip.\n",
            "[nltk_data]    | Downloading package webtext to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/webtext.zip.\n",
            "[nltk_data]    | Downloading package wmt15_eval to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping models/wmt15_eval.zip.\n",
            "[nltk_data]    | Downloading package word2vec_sample to\n",
            "[nltk_data]    |     /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping models/word2vec_sample.zip.\n",
            "[nltk_data]    | Downloading package wordnet to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package wordnet2021 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package wordnet2022 to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/wordnet2022.zip.\n",
            "[nltk_data]    | Downloading package wordnet31 to /root/nltk_data...\n",
            "[nltk_data]    | Downloading package wordnet_ic to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/wordnet_ic.zip.\n",
            "[nltk_data]    | Downloading package words to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/words.zip.\n",
            "[nltk_data]    | Downloading package ycoe to /root/nltk_data...\n",
            "[nltk_data]    |   Unzipping corpora/ycoe.zip.\n",
            "[nltk_data]    | \n",
            "[nltk_data]  Done downloading collection all\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ],
      "source": [
        "nltk.download('all')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "amt8cwhNjU_9"
      },
      "outputs": [],
      "source": [
        "def sentiment_analysis(prod):\n",
        "    prod['combined_text'] = prod['title'].map(str)\n",
        "\n",
        "    # applying all of these functions to the our dataframe \n",
        "    prod['combined_text'] = prod['combined_text'].map(clean_text)\n",
        "    prod['tokens'] = prod['combined_text'].map(tokenize)\n",
        "    prod['tokens'] = prod['tokens'].map(remove_stopwords)\n",
        "    prod['lems'] = prod['tokens'].map(lemmatize)\n",
        "    sia = SIA()\n",
        "    results = []\n",
        "    for line in prod['lems']:\n",
        "        pol_score = sia.polarity_scores(line)\n",
        "        pol_score['lems'] = line\n",
        "        results.append(pol_score)\n",
        "    headlines_polarity = pd.DataFrame.from_records(results)\n",
        "    temp = []\n",
        "    # for line in prod['branch']:\n",
        "        # temp.append(line)\n",
        "    # headlines_polarity['branch'] = temp\n",
        "    headlines_polarity['label'] = 0\n",
        "    headlines_polarity.loc[headlines_polarity['compound'] > 0.2, 'label'] = 1\n",
        "    headlines_polarity.loc[headlines_polarity['compound'] < -0.2, 'label'] = -1\n",
        "    headlines_polarity['word_count'] = headlines_polarity['lems'].apply(lambda x: len(str(x).split()))\n",
        "    headlines_polarity.head()\n",
        "    # gk = headlines_polarity.groupby(['branch', 'label'])\n",
        "    # fk = headlines_polarity.groupby('branch')['compound'].mean()\n",
        "    # fk = fk.to_frame()\n",
        "    result = [prod, headlines_polarity]\n",
        "    headlines_polarity = headlines_polarity.rename_axis(index=None)\n",
        "    return pd.merge(prod, headlines_polarity, on=[\"lems\"], how=\"left\")\n",
        "    "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "c2edY3CuN9Nl"
      },
      "outputs": [],
      "source": [
        "from datetime import date\n",
        "\n",
        "def outsource_news():\n",
        "    googleNewsByStreet()\n",
        "    prod = pd.concat(final)\n",
        "    prod = prod.drop_duplicates('title', keep='first')\n",
        "    print(prod)\n",
        "    status_val.append(30)\n",
        "\n",
        "    final_prod = sentiment_analysis(prod)\n",
        "\n",
        "    # mail_data(final_prod) & upload_data_complete(final_prod)\n",
        "      \n",
        "    final_prod = final_prod.replace(np.nan,'',regex=True)\n",
        "\n",
        "    # forecast_keywords = ['sale', 'sport', 'beverage', 'retail', 'vendor', 'market', 'morrisons', 'tesco', 'coles', 'business', 'shopping', 'weather', \n",
        "    #                      'parties', 'events', 'walmart']\n",
        "\n",
        "    second_keywords = ['bank holiday', 'heatwave', 'inflation', 'street party', 'rainfall', 'snow', 'retail', 'beverage', 'tesco', 'walmart', 'morrisons', 'weather', \n",
        "                       'brc', 'mothers day', 'new store launch', 'lidl', 'homebase', 'walmart', 'new tesco store', 'coles', 'supermarket', 'shoppers', 'store', 'grocery', 'strike', 'holiday'\n",
        "                       'shops', 'markets','holiday', 'lockdown','grocery sales', 'carnival', 'festival', 'party', \"sainsbury\", \"supply chain\", \"flood\", \"wendys\",\n",
        "                       'ocado', 'spencer', 'asda']                    \n",
        "\n",
        "    remove_keywords = ['accident', 'incident', 'injury', 'political', 'police', 'death', 'traffic', 'lord', 'war', 'actor', 'movie', 'star', 'lord', 'sex', 'gay',\n",
        "                       'fight', 'crash', 'life', 'weapons', 'dating', 'radio', 'tv', 'guinness', 'husband', 'fashion', 'attack']\n",
        "\n",
        "    store_keywords = ['opens', 'closes', 'closed', 'opened', 'open', 'close', \n",
        "                      'shut', 'confining', 'unopen', 'opening',\n",
        "                      'close down', 'closing', 'shut down', 'conclude', 'ending', 'shutdown', 'closedown',\n",
        "                      'closure', 'temporary', 'extended', 'shutting', 'launch', 'shuts', 'closures', 'roadworks', 'streetworks']\n",
        "\n",
        "    store_remove_keywords = ['ftse', 'pubs', 'pub', 'life', 'stocks', 'earnings', 'dining', 'restaurants', 'stock', 'rocket', 'fashion', 'restaurant',\n",
        "                             'letter', 'bills', 'investment', 'childrenswear', 'blizzard', 'infamous', 'qualifying', 'sports', 'bar', 'cafe', \n",
        "                             'technology', 'dental', 'boobs', 'school', 'flixbus', 'allegations', 'pharmacy', 'attack', 'driver', 'fitness', 'students',\n",
        "                             'charities']\n",
        "                  \n",
        "    competitor_keywords = ['tesco', 'wendys', 'lidl', 'sainsburys', 'sainsbury', 'aldi', 'morrisons', 'spencer', 'asda', 'supermarket',\n",
        "                            'co', 'ocado', 'sparks', 'b&m', 'iceland', 'waitrose']\n",
        "\n",
        "    print(final_prod)\n",
        "\n",
        "    for index, row in final_prod.iterrows():\n",
        "      if (len(np.intersect1d(row['tokens'], store_keywords)) == 0):\n",
        "        # if(len(np.intersect1d(row['tokens'], competitor_keywords)) == 0):\n",
        "        final_prod.drop(index=index, axis=0, inplace=True)\n",
        "\n",
        "    for index, row in final_prod.iterrows():\n",
        "      for value in row['tokens']:\n",
        "        val = value.capitalize()\n",
        "        try:\n",
        "            final_prod.at[index,'bu_num'] = branch_keyword_bu_num[val]\n",
        "            final_prod.at[index,'branch'] = val\n",
        "        except:\n",
        "            n = 0\n",
        "\n",
        "    final_prod = final_prod.drop_duplicates('title', keep='first')\n",
        "    final_prod = final_prod.drop_duplicates('lems', keep='first')\n",
        "    final_prod = final_prod.drop_duplicates('tokens', keep='first')\n",
        "\n",
        "    final_prod['title'] = final_prod['title'].astype(str)\n",
        "\n",
        "    final_prod['competitor_evt_indchar'] = ['Yes' if(len(np.intersect1d(x,competitor_keywords)) > 0) else 'No' for x in final_prod['tokens']]\n",
        "\n",
        "    counter_guid = int(date.today().strftime(\"%Y%m%d\"))\n",
        "    final_prod['efsevt_guid'] = [(counter_guid*1000)+i for i in range(len(final_prod))]\n",
        "\n",
        "    print(final_prod.dtypes)\n",
        "    print(final_prod_events.dtypes)\n",
        "\n",
        "    foriegn_key = []\n",
        "\n",
        "    for index, row in final_prod.iterrows():\n",
        "      flag = False\n",
        "      for index_event, row_event in final_prod_events.iterrows():\n",
        "        if(row['keyword'] != '' ):\n",
        "          if(row['keyword'] in row_event['NAME']):\n",
        "            print(row['keyword'],row_event['NAME'])\n",
        "            foriegn_key.append(row_event['GUID'])\n",
        "            flag = True\n",
        "      if(flag == False):\n",
        "        foriegn_key.append(0)\n",
        "\n",
        "    print(foriegn_key)\n",
        "\n",
        "    final_prod['guid'] = [(counter_guid*2000)+i for i in range(len(final_prod))]\n",
        "    final_prod['fixed_annual_ind'] = 'n'\n",
        "    final_prod['perm_env_ind'] = 'n'\n",
        "    final_prod['cancelled_ind'] = 'n'\n",
        "    final_prod['create_user'] = ''\n",
        "    final_prod['update_user'] = ''\n",
        "    final_prod['perm_env_ind'] = 'n'    \n",
        "    final_prod['crt_timestamp'] = date.today()\n",
        "    final_prod['upd_timestamp'] = date.today()\n",
        "\n",
        "\n",
        "    final_prod.rename(columns = {'link':'source_of_event'}, inplace = True)\n",
        "    final_prod[[\"datetime\"]] = final_prod[[\"datetime\"]].astype(str)\n",
        "    final_prod.columns = final_prod.columns.str.upper()\n",
        "\n",
        "    final_prod.to_csv('Events.csv', mode='a', index=False, header=False)\n",
        "    return final_prod\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KBR08rg-jxHV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d985c599-973f-4e1a-bd26-4b2b92bcdc3f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: geopy in /usr/local/lib/python3.10/dist-packages (2.3.0)\n",
            "Requirement already satisfied: geographiclib<3,>=1.52 in /usr/local/lib/python3.10/dist-packages (from geopy) (2.0)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pgeocode\n",
            "  Downloading pgeocode-0.4.0-py3-none-any.whl (9.7 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from pgeocode) (2.27.1)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from pgeocode) (1.22.4)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from pgeocode) (1.5.3)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->pgeocode) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->pgeocode) (2022.7.1)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->pgeocode) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->pgeocode) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->pgeocode) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->pgeocode) (3.4)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.1->pandas->pgeocode) (1.16.0)\n",
            "Installing collected packages: pgeocode\n",
            "Successfully installed pgeocode-0.4.0\n"
          ]
        }
      ],
      "source": [
        "!pip install geopy\n",
        "!pip install pgeocode\n",
        "\n",
        "from geopy.geocoders import Photon, GoogleV3, Nominatim\n",
        "import pgeocode\n",
        "from math import cos, asin, sqrt, pi\n",
        "\n",
        "def distance(lat1, lon1, lat2, lon2):\n",
        "    p = pi/180\n",
        "    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2\n",
        "    return round(12742 * asin(sqrt(a)),2)\n",
        "\n",
        "\n",
        "def place_distance(string1,string2):\n",
        "    try:\n",
        "      geolocator_addr = Nominatim(user_agent=\"http\")\n",
        "      # place = \"Lidl,Bath\"\n",
        "      # place_2 = \"Waitrose,Bath\"\n",
        "      place = string1 + \",\" + string2\n",
        "      place_2 = \"Waitrose,\" + string2\n",
        "      # location = geolocator.geocode(place)\n",
        "      pin = geolocator_addr.geocode(place)\n",
        "      pin_2 = geolocator_addr.geocode(place_2)\n",
        "      # print(location)\n",
        "      print(pin)\n",
        "      print(pin_2)\n",
        "      print(pin.raw['lat'],pin.raw['lon'],pin_2.raw['lat'],pin_2.raw['lon'])\n",
        "    except:\n",
        "      return 'N/A'\n",
        "    \n",
        "    return distance(float(pin.raw['lat']),float(pin.raw['lon']),float(pin_2.raw['lat']),float(pin_2.raw['lon']))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pretty-html-table\n",
        "!pip install pyshorteners\n",
        "\n",
        "import smtplib, ssl\n",
        "from smtplib import SMTP\n",
        "from email.mime.text import MIMEText\n",
        "from email.mime.multipart import MIMEMultipart\n",
        "import pandas as pd\n",
        "from pretty_html_table import build_table\n",
        "from pyshorteners import Shortener\n",
        "from io import StringIO\n",
        "from email.mime.application import MIMEApplication\n",
        "from datetime import date, timedelta\n",
        "\n",
        "def mail_data(final_prod):\n",
        "  port = 465  # For SSL\n",
        "  context = ssl.create_default_context()\n",
        "  mail_df = pd.DataFrame()\n",
        "  mail_df[\"TITLE\"] = final_prod[\"TITLE\"]\n",
        "  mail_df[\"BRANCH\"] = final_prod[\"BRANCH\"]\n",
        "  mail_df[\"SOURCE\"] = final_prod[\"MEDIA\"]\n",
        "  mail_df[\"DATETIME\"] = final_prod[\"DATETIME\"]\n",
        "  mail_df[\"BRANCH_NUM\"] = final_prod[\"BU_NUM\"]\n",
        "\n",
        "  distance_arr = []\n",
        "  for index, row in final_prod.iterrows():\n",
        "    if(row[\"KEYWORD\"] and row[\"BRANCH\"]):\n",
        "        distance_arr.append(place_distance(row[\"KEYWORD\"], row[\"BRANCH\"]))\n",
        "  mail_df[\"DISTANCE IN MILES\"] = distance_arr\n",
        "  \n",
        "  urls = []\n",
        "  for index,row in final_prod.iterrows(): \n",
        "      x = Shortener().tinyurl.short(row[\"SOURCE_OF_EVENT\"])\n",
        "      urls.append(x)\n",
        "  \n",
        "  mail_df[\"LINK\"] = urls\n",
        "\n",
        "  for index, row in mail_df.iterrows():\n",
        "    if(row[\"DISTANCE IN MILES\"] != 'N/A'):\n",
        "      if(row[\"DISTANCE IN MILES\"] > 25):\n",
        "          mail_df.drop(index=index, axis=0, inplace=True)\n",
        "\n",
        "  html_table = mail_df.to_html(index=False, classes='example-table')\n",
        "\n",
        "  text = f\"Hello Alex and Olga,\\n Herewith attaching the events captured for all the competitors (core event types) including all the branches from \" + (date.today() - timedelta(days = 1)).strftime(\"%d-%m-%Y\") + \" to \" + date.today().strftime(\"%d-%m-%Y\") + \" which are auto-generated from the script.\\n\\n\\nThanks And Regards,\\nSashank L\\n\\n\\n\"\n",
        "\n",
        "\n",
        "  print(mail_df)\n",
        "\n",
        "  html_table = html_table.replace('<th>', '<th style=\"padding: 10px 90px 10px 90px;\">', 1)\n",
        "\n",
        "# HTML Styling\n",
        "  html = f'''\n",
        "<html>\n",
        "<head>\n",
        "    <style>\n",
        "        table.example-table th{{\n",
        "              padding: 10px;\n",
        "              text-align: center;\n",
        "              background-color: #FFFFFF;\n",
        "              font-weight: bold;\n",
        "              font-size: 14px;\n",
        "              width: 400px;\n",
        "          }}\n",
        "\n",
        "          table.example-table th:first-child {{\n",
        "            padding: 20px 100px 20px 100px; /* Set the desired width for the fourth column */\n",
        "          }}\n",
        "\n",
        "          table.example-table td {{\n",
        "            padding: 5px;\n",
        "            color: black;\n",
        "            font-size: 12px;\n",
        "            width: 400px;\n",
        "            font-family: Century Gothic, sans-serif;\n",
        "          }}\n",
        "\n",
        "        /* Add custom styles here */\n",
        "    </style>\n",
        "</head>\n",
        "<body>\n",
        "      <pre>{text}</pre>\n",
        "        {html_table}\n",
        "</body>\n",
        "</html>\n",
        "'''\n",
        "\n",
        "  part1 = MIMEText(html, 'html')\n",
        "  msg = MIMEMultipart(\"alternative\")\n",
        "  msg['Subject'] = \"Automated Event Capturing Model\"\n",
        "  # recipients = ['amit.kumbhar@johnlewis.co.uk', 'mitali.patel@johnlewis.co.uk', \"alex.nicola@waitrose.co.uk\", \"olga.jakobsone@waitrose.co.uk\"]\n",
        "  recipients = ['sashank99narayan@gmail.com']\n",
        "  msg['To'] = \", \".join(recipients)\n",
        "  msg.attach(part1)\n",
        "\n",
        "  textStream = StringIO()\n",
        "  mail_df.to_csv(textStream,index=False)\n",
        "  attachment = MIMEApplication(textStream.getvalue())\n",
        "  attachment['Content-Disposition'] = 'attachment; filename=\"{}\"'.format(date.today().strftime(\"%d-%m-%Y\") + \"_Events.csv\")\n",
        "  msg.attach(attachment)\n",
        "\n",
        "  with smtplib.SMTP_SSL(\"smtp.gmail.com\", port, context=context) as server:\n",
        "      print(\"IN\")\n",
        "      server.login(\"sashank99narayan@gmail.com\", \"tauvozkdtqbkqycf\")\n",
        "      server.sendmail(\"sashank99narayan@gmail.com\", recipients, msg.as_string())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cFBGJI7DBYMD",
        "outputId": "6dcad084-84e0-4a30-92be-95b202e7f4e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pretty-html-table\n",
            "  Downloading pretty_html_table-0.9.16-py3-none-any.whl (6.8 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from pretty-html-table) (1.5.3)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->pretty-html-table) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->pretty-html-table) (2022.7.1)\n",
            "Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.10/dist-packages (from pandas->pretty-html-table) (1.22.4)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.1->pandas->pretty-html-table) (1.16.0)\n",
            "Installing collected packages: pretty-html-table\n",
            "Successfully installed pretty-html-table-0.9.16\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyshorteners\n",
            "  Downloading pyshorteners-1.0.1.tar.gz (10.0 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from pyshorteners) (2.27.1)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->pyshorteners) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->pyshorteners) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->pyshorteners) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->pyshorteners) (3.4)\n",
            "Building wheels for collected packages: pyshorteners\n",
            "  Building wheel for pyshorteners (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyshorteners: filename=pyshorteners-1.0.1-py3-none-any.whl size=17479 sha256=497d1587f1bec9bcc84a2e13d913ee8312a2b81f1ade4d6a816dfe2646f86af2\n",
            "  Stored in directory: /root/.cache/pip/wheels/d5/ff/b3/16d8906f92ab0b042f76a4696fcea11d291d79a2b3a3de1e78\n",
            "Successfully built pyshorteners\n",
            "Installing collected packages: pyshorteners\n",
            "Successfully installed pyshorteners-1.0.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X3FYrkChWAUo",
        "outputId": "afbd9494-64a0-46b9-d1e0-4e82bbe520a5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                               title  desc          date  \\\n",
            "0  Love Island contestants revealed ahead of seri...  None  17 hours ago   \n",
            "1  Sam Allardyce says sorry after Leeds relegated...  None  23 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 15:04:31.116728   \n",
            "1 2023-05-29 09:04:31.117246   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMicmh0dHBzOi8vd3d...   \n",
            "1  news.google.com/./articles/CBMiSWh0dHBzOi8vY2E...   \n",
            "\n",
            "                                                 img                 media  \\\n",
            "0  https://lh3.googleusercontent.com/ewf6wCS_XneS...  Peterborough Matters   \n",
            "1  https://lh3.googleusercontent.com/proxy/_rGga2...   Yahoo Movies Canada   \n",
            "\n",
            "   site keyword        branch  bu_num  \n",
            "0  None   Tesco  Peterborough     531  \n",
            "1  None   Tesco  Peterborough     531  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                               title  desc          date  \\\n",
            "0  Sam Allardyce says sorry after Leeds relegated...  None  23 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 09:04:34.190648   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMiSWh0dHBzOi8vY2E...   \n",
            "\n",
            "                                                 img                media  \\\n",
            "0  https://lh3.googleusercontent.com/proxy/_rGga2...  Yahoo Movies Canada   \n",
            "\n",
            "   site  keyword        branch  bu_num  \n",
            "0  None  Walmart  Peterborough     531  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                               title  desc          date  \\\n",
            "0  Rescheduled Peterborough Speedway Opener Draws...  None  10 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 22:05:08.897813   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMiXmh0dHBzOi8vd3d...   \n",
            "\n",
            "                                                 img  \\\n",
            "0  https://encrypted-tbn0.gstatic.com/faviconV2?u...   \n",
            "\n",
            "                          media  site           keyword        branch  bu_num  \n",
            "0  Inside Track Motorsport News  None  Marks & Spencers  Peterborough     531  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                               title  desc          date  \\\n",
            "0  2023 Memorial Cup: 3 Takeaways From Blazers’ W...  None  18 hours ago   \n",
            "1  Search for Disappeared victims of Troubles 'wi...  None  14 hours ago   \n",
            "2  Barnsley 0 Sheffield Wednesday 1: Josh Windass...  None  15 hours ago   \n",
            "3  Another footballer signs up for Love Island ah...  None  21 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 14:05:11.168439   \n",
            "1 2023-05-29 18:05:11.168753   \n",
            "2 2023-05-29 17:05:11.169021   \n",
            "3 2023-05-29 11:05:11.169279   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMic2h0dHBzOi8vd3d...   \n",
            "1  news.google.com/./articles/CBMif2h0dHBzOi8vd3d...   \n",
            "2  news.google.com/./articles/CBMiZWh0dHBzOi8vd3d...   \n",
            "3  news.google.com/./articles/CBMiZGh0dHBzOi8vZmF...   \n",
            "\n",
            "                                                 img                 media  \\\n",
            "0  https://lh3.googleusercontent.com/eFMr8kd_JkOE...            Yardbarker   \n",
            "1  https://lh3.googleusercontent.com/ewf6wCS_XneS...  Peterborough Matters   \n",
            "2  https://lh3.googleusercontent.com/aEbEY0gBYB0R...            The US Sun   \n",
            "3  https://encrypted-tbn2.gstatic.com/faviconV2?u...             FanBanter   \n",
            "\n",
            "   site     keyword        branch  bu_num  \n",
            "0  None  Morrison's  Peterborough     531  \n",
            "1  None  Morrison's  Peterborough     531  \n",
            "2  None  Morrison's  Peterborough     531  \n",
            "3  None  Morrison's  Peterborough     531  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Empty DataFrame\n",
            "Columns: [keyword, branch, bu_num]\n",
            "Index: []\n",
            "            keyword        branch  bu_num  \\\n",
            "0             Tesco  Peterborough     531   \n",
            "1             Tesco  Peterborough     531   \n",
            "3  Marks & Spencers  Peterborough     531   \n",
            "4        Morrison's  Peterborough     531   \n",
            "5        Morrison's  Peterborough     531   \n",
            "6        Morrison's  Peterborough     531   \n",
            "7        Morrison's  Peterborough     531   \n",
            "\n",
            "                                               title  desc          date  \\\n",
            "0  Love Island contestants revealed ahead of seri...  None  17 hours ago   \n",
            "1  Sam Allardyce says sorry after Leeds relegated...  None  23 hours ago   \n",
            "3  Rescheduled Peterborough Speedway Opener Draws...  None  10 hours ago   \n",
            "4  2023 Memorial Cup: 3 Takeaways From Blazers’ W...  None  18 hours ago   \n",
            "5  Search for Disappeared victims of Troubles 'wi...  None  14 hours ago   \n",
            "6  Barnsley 0 Sheffield Wednesday 1: Josh Windass...  None  15 hours ago   \n",
            "7  Another footballer signs up for Love Island ah...  None  21 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 15:04:31.116728   \n",
            "1 2023-05-29 09:04:31.117246   \n",
            "3 2023-05-29 22:05:08.897813   \n",
            "4 2023-05-29 14:05:11.168439   \n",
            "5 2023-05-29 18:05:11.168753   \n",
            "6 2023-05-29 17:05:11.169021   \n",
            "7 2023-05-29 11:05:11.169279   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMicmh0dHBzOi8vd3d...   \n",
            "1  news.google.com/./articles/CBMiSWh0dHBzOi8vY2E...   \n",
            "3  news.google.com/./articles/CBMiXmh0dHBzOi8vd3d...   \n",
            "4  news.google.com/./articles/CBMic2h0dHBzOi8vd3d...   \n",
            "5  news.google.com/./articles/CBMif2h0dHBzOi8vd3d...   \n",
            "6  news.google.com/./articles/CBMiZWh0dHBzOi8vd3d...   \n",
            "7  news.google.com/./articles/CBMiZGh0dHBzOi8vZmF...   \n",
            "\n",
            "                          media  \n",
            "0          Peterborough Matters  \n",
            "1           Yahoo Movies Canada  \n",
            "3  Inside Track Motorsport News  \n",
            "4                    Yardbarker  \n",
            "5          Peterborough Matters  \n",
            "6                    The US Sun  \n",
            "7                     FanBanter  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-17-e8bb4f847922>:15: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.\n",
            "  data = data.append(df, ignore_index=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            keyword        branch  bu_num  \\\n",
            "0             Tesco  Peterborough     531   \n",
            "1             Tesco  Peterborough     531   \n",
            "2  Marks & Spencers  Peterborough     531   \n",
            "3        Morrison's  Peterborough     531   \n",
            "4        Morrison's  Peterborough     531   \n",
            "5        Morrison's  Peterborough     531   \n",
            "6        Morrison's  Peterborough     531   \n",
            "\n",
            "                                               title desc          date  \\\n",
            "0  Love Island contestants revealed ahead of seri...       17 hours ago   \n",
            "1  Sam Allardyce says sorry after Leeds relegated...       23 hours ago   \n",
            "2  Rescheduled Peterborough Speedway Opener Draws...       10 hours ago   \n",
            "3  2023 Memorial Cup: 3 Takeaways From Blazers’ W...       18 hours ago   \n",
            "4  Search for Disappeared victims of Troubles 'wi...       14 hours ago   \n",
            "5  Barnsley 0 Sheffield Wednesday 1: Josh Windass...       15 hours ago   \n",
            "6  Another footballer signs up for Love Island ah...       21 hours ago   \n",
            "\n",
            "                    datetime  \\\n",
            "0 2023-05-29 15:04:31.116728   \n",
            "1 2023-05-29 09:04:31.117246   \n",
            "2 2023-05-29 22:05:08.897813   \n",
            "3 2023-05-29 14:05:11.168439   \n",
            "4 2023-05-29 18:05:11.168753   \n",
            "5 2023-05-29 17:05:11.169021   \n",
            "6 2023-05-29 11:05:11.169279   \n",
            "\n",
            "                                                link  \\\n",
            "0  news.google.com/./articles/CBMicmh0dHBzOi8vd3d...   \n",
            "1  news.google.com/./articles/CBMiSWh0dHBzOi8vY2E...   \n",
            "2  news.google.com/./articles/CBMiXmh0dHBzOi8vd3d...   \n",
            "3  news.google.com/./articles/CBMic2h0dHBzOi8vd3d...   \n",
            "4  news.google.com/./articles/CBMif2h0dHBzOi8vd3d...   \n",
            "5  news.google.com/./articles/CBMiZWh0dHBzOi8vd3d...   \n",
            "6  news.google.com/./articles/CBMiZGh0dHBzOi8vZmF...   \n",
            "\n",
            "                          media  \\\n",
            "0          Peterborough Matters   \n",
            "1           Yahoo Movies Canada   \n",
            "2  Inside Track Motorsport News   \n",
            "3                    Yardbarker   \n",
            "4          Peterborough Matters   \n",
            "5                    The US Sun   \n",
            "6                     FanBanter   \n",
            "\n",
            "                                       combined_text  \\\n",
            "0  love island contestants revealed ahead of seri...   \n",
            "1  sam allardyce says sorry after leeds relegated...   \n",
            "2  rescheduled peterborough speedway opener draws...   \n",
            "3  memorial cup  takeaways from blazers win over ...   \n",
            "4  search for disappeared victims of troubles wil...   \n",
            "5  barnsley  sheffield wednesday  josh windass he...   \n",
            "6  another footballer signs up for love island ah...   \n",
            "\n",
            "                                              tokens  \\\n",
            "0  [love, island, contestants, revealed, ahead, s...   \n",
            "1  [sam, allardyce, says, sorry, leeds, relegated...   \n",
            "2  [rescheduled, peterborough, speedway, opener, ...   \n",
            "3    [memorial, cup, takeaways, blazers, win, petes]   \n",
            "4  [search, disappeared, victims, troubles, never...   \n",
            "5  [barnsley, sheffield, wednesday, josh, windass...   \n",
            "6  [another, footballer, signs, love, island, ahead]   \n",
            "\n",
            "                                                lems    neg    neu    pos  \\\n",
            "0  love island contestant revealed ahead series l...  0.000  0.588  0.412   \n",
            "1  sam allardyce say sorry leeds relegated apolog...  0.110  0.424  0.466   \n",
            "2  rescheduled peterborough speedway opener draw ...  0.000  0.645  0.355   \n",
            "3             memorial cup takeaway blazer win petes  0.000  0.568  0.432   \n",
            "4       search disappeared victim trouble never stop  0.633  0.189  0.178   \n",
            "5  barnsley sheffield wednesday josh windass head...  0.000  0.599  0.401   \n",
            "6          another footballer sign love island ahead  0.000  0.543  0.457   \n",
            "\n",
            "   compound  label  word_count  \n",
            "0    0.6369      1           7  \n",
            "1    0.6369      1           8  \n",
            "2    0.5106      1           7  \n",
            "3    0.5859      1           6  \n",
            "4   -0.5875     -1           6  \n",
            "5    0.7717      1          12  \n",
            "6    0.6369      1           6  \n",
            "keyword                           object\n",
            "branch                            object\n",
            "bu_num                             int64\n",
            "title                             object\n",
            "desc                              object\n",
            "date                              object\n",
            "datetime                  datetime64[ns]\n",
            "link                              object\n",
            "media                             object\n",
            "combined_text                     object\n",
            "tokens                            object\n",
            "lems                              object\n",
            "neg                              float64\n",
            "neu                              float64\n",
            "pos                              float64\n",
            "compound                         float64\n",
            "label                              int64\n",
            "word_count                         int64\n",
            "competitor_evt_indchar           float64\n",
            "efsevt_guid                      float64\n",
            "dtype: object\n",
            "Series([], dtype: object)\n",
            "[]\n",
            "Empty DataFrame\n",
            "Columns: [TITLE, BRANCH, SOURCE, DATETIME, BRANCH_NUM, DISTANCE IN MILES, LINK]\n",
            "Index: []\n",
            "IN\n"
          ]
        }
      ],
      "source": [
        "if __name__ == '__main__':\n",
        "  final_prod = outsource_news()\n",
        "  mail_data(final_prod)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# from datetime import date\n",
        "# from google.colab import auth\n",
        "# auth.authenticate_user()\n",
        "# from google.auth import default\n",
        "# creds, _ = default()\n",
        "# from gspread_dataframe import set_with_dataframe\n",
        "# import gspread\n",
        "# import pandas as pd\n",
        "# from flask import Flask, jsonify, Response, request\n",
        "# from flask_ngrok import run_with_ngrok\n",
        "# from json import loads\n",
        "\n",
        "# def validate():\n",
        "    # gc = gspread.authorize(creds)\n",
        "    # worksheet = gc.open(\"26/05/2023\").sheet1\n",
        "    # final_prod = pd.DataFrame(data=worksheet.get_all_records())\n",
        "    ##mail_data(final_prod)\n",
        "    # print(final_prod.to_json(orient=\"index\"))\n",
        "    # return Response(final_prod.to_json(orient=\"index\"), mimetype='application/json')\n",
        "\n",
        "# validate()"
      ],
      "metadata": {
        "id": "U_AJv-tYA9ZE"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "provenance": []
    },
    "gpuClass": "standard",
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.4"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
