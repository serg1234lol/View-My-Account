#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
from time import sleep
import datetime
import sys
import random
import json
import yaml
import ymlconfig
import os
# Trying to make this work in mac
# import imp
# InstagramAPI = imp.load_source('InstagramAPI', '/usr/local/lib/python2.7/site-packages/InstagramAPI/InstagramAPI.py')
# InstagramAPI.MyClass()

def get_absolute_path(relative_path):
    dirname = os.path.dirname(__file__)
    print dirname
    filename = os.path.join(dirname, relative_path)
    print filename
    return filename

def load_config():
    config_path = "/etc/ig/cf.yml"
    cfg = ymlconfig.load_file(config_path)
    """
    user: XXX
    password: YYY
    """
    return cfg

def load_config(path):
    config_path = path
    cfg = ymlconfig.load_file(config_path)
    print(str(getDateNow()) +" This is the account used: " + str(config_path))
    """
    user: XXX
    password: YYY
    """
    return cfg

modelsInstagramAccounts = {
"worldsexymodels" : 2062359584,
"topclass_models" : 2876923303,
"just_hot_modelss" : 2933075018,
"worldsbestmodelz" : 2078170244,
"thaimodels" : 401942097,
"asian_girlsonly" : 6085159445,
"modelsasia" : 6170419243,
"modelstarz_" : 1338968500,
"modelstatus6" : 1102461365,
"modela_asia" : 1552262221,
"top_sexy_babes" : 5486953135,
"sexy.college.babes" : 5406740518,
"sexybollywoodbabes" : 4785862616,
#only 1000 followers
#"world_of_babes_" : 7310362284,
"insta.asian.babes" : 5866463945,
"babesdailyofficial" : 2286864765,
"babesofasia" : 3564238293,
"hot.asian.babes" : 7080632348,
"babes_hottest" : 6264559907,
"babesasia" : 6146767332,
"babemodels" : 470026323,
"sexy_asian_girls_gram" : 5799081624,
"sexyhotgirls_official" : 707940375,
"sexygirlasian_" : 1980034995,
"sexypinays" : 3515733764,
"popular_beauties" : 2133805997,
"sexy_hot_beauties" : 5776380812,
"world__of__latinas" : 5060402023,
"hot_asian_beauty" : 7036553804,
"asiansnextdoor1" : 1983451062,
"asianbaddazz" : 3018595549,
"sexy.hot.asian.models" : 7309287546,
# only 1000 followers
#"asiangirls09" : 7366587105,
# "babegirls_insta" : 5779744439,
# "babess.from.heaven" : 6519014935,
# "japan.best.girls" : 5595012322,
"sexy_igmodels" : 1558507012,
"sexy_cute_thaigirls" : 4745344194,
"realbabeslove" : 6997757676,
"orientalvixens" : 46381251,
"asiantwerkqueen" : 321009618,
"asianbarbiez" : 6020717992,
"asiangirlfriends" : 5965315053,
"instababes.asian" : 4471893432,
"instarealasians" : 3988204068,
"gifted_filipinas" : 5566360438,
"universe_of_asians" : 5959973437,
"sweet.asian.girls" : 6693456858,
"jennakaey" : 246493572,
"global_asian_beauties" : 5788674536,
"asian_sexy_squad" : 7152079441 ,
#"queenasians" : 7850516807, 12000
"daily_asians" : 7999182413,
"bangingasians" : 997716286,
"bellaasians" : 6792061391,
"asianhottiez" : 3154849640,
"world__of__beauties" : 5422249978,
"serverbeauties" : 398989830,
"world_of_asians" : 2000810021,
"world__of__blondes" : 5060402023,
"noagold18" : 702483823, # brunnete
"coralzitker" : 223199904, # brunnete
"rhiannondarney" : 24411410, # blonde
"vyvan.le" : 1956773381,
"1bambei" : 284495008,
"mintasianz" : 1240218494,
"yeccong_" : 1688886813,
"lizwenya" : 250939171,
"olga.rebrikova" : 3118094966,
"_bitnara_" : 5849529154
}

foodInstagramAccounts = {
"adikosh123" : 20253508,
"yolanda_gampp" : 213175269,
"foodiesince96" : 3489049832,
"dradevsfood" : 26230233,
"eden_table" : 1714071113,
"siralikebap" : 3645319047,
"silviaribeirogourmet" : 353498410,
"food_oclock" : 1283027662,
"5boroughfoodie" : 2111051564,
#"kunefecisadik" : 5611919495, 9000
"tnppa" : 178001183,
"thenaughtyfork" : 1276053734,
#"c.ash.tray" : 233068424,
"tastemade" : 227921678,
"howeat219" : 4029942073,
"devourpower" : 616063402,
"hergun1yer" : 4475188342,
"ginyuudai" : 2186246883,
"ganna_kostroma" : 290138230,
"antalyagurmesii" : 6234668727,
"ptmangkut" : 316398450,
"delicious_blog_95" : 3651562381,
"mrcookingpanda" : 3665077588,
"rickbolzani" : 568319455,
"vkusnaya_eda_35" : 4659356722,
"yadala_organic_natural" : 1371782116,
"foodbymay" : 55241426,
"harbiyiyorum" : 523667021,
"cookingbypat" : 974341151,
"cedricgrolet" : 732510392,
"foodnetwork" : 25742083,
"foodie.munchies" : 14619328,
"fitwaffle" : 2089781309,
"recipegirl" : 4633196,
"foodyfetish" : 2036672771,
"lennardy" : 41858353,
"poiluang_cooking" : 3253259146,
"amauryguichon" : 203296913,
#"sightsandbitesnyc" : 6263336994,
"endermutfakta" : 195699894,
"sukrankaymak" : 323955377,
"lamonnyel" : 3163318730,
"fooddolls" : 2281927264,
"yemek_askim" : 1356803900,
"beiny_" : 5630534591,
"rawvana" : 27219869,
"som_e92" : 1116404072,
"pecolly_official" : 2313667073,
"cznburak" : 303947497,
"irresistiblesfood" : 6392122860,
"60s.yummy" : 7754388862,
"twisted" : 1736358215,
"cookist" : 6820668083,
"flavorfulrecipes" : 6637372271,
"hellofresh" : 221770801,
"tastyvegetarian" : 4947648586,
"buzzfeedtasty" : 2125506698,
"cookat__" : 3507772515,
#"_vegan_val_" : 540312669,
"tiphero" : 2292551457,
"channeldelish" : 8187785056
}

bulldogsInstagramAccounts = {
"puppystagrams" : 1559136659,
"bulldogstuff" : 5905060,
"sgt_bulldog" : 16881198,
"jorge_thebulldog" : 4028271238,
"bullyrazzis" : 273549266,
"bulldog__diesel" : 5840535297,
"pieter.shirley" : 2538045062,
"weheart.bulldogs" : 5443333159,
"butter_the_bulldog" : 2071091186,
"titon_and_fiona" : 2376505933,
# "winston_da_potato" : 7364595221,
"bulldogleon0421" : 1794915685,
"bulldogoclock" : 481645069,
"matildarose_thebulldog" : 3289230028,
# "windsor_roman_king" : 8150253653,
#  "the_bulldog_lebowski" : 6680502408,
"missdafne_" : 2293719512, # 4000 users
# "_bonniethebulldog" : 7219766877,
"bulldogwalter" : 1933701573,
# "theroyalprinceteo" : 4867076231,
#"rudynroman" : 6712684669,
#"princesspugwhiteknightbulldog" : 2946619416,
"arthurzinhoeskinazi" : 7909345642,
#"the.love.of.bulldog" : 8059976371, # 4000 users
"meubulldogingles" : 593888211, # 7000 users
"bullyfame" : 1048181764,
# "chestersocks" : 7590517547,
"rocco_and_duca" : 1686354279,
# "lets_go_hank" : 7866472418,
# "nala_and_coco_" : 7579390058,
"minibulldogsrus" : 195898640,
# "bulldog_rubyred" : 6000258226,
# "maca_bulldog" : 8376579386,
# "dieselthedawg" : 251973778, # 3000 users
# "kung_fu_ken_ken_" : 6555363773,
"beefybulldogs" : 19882799, # 4000 users
#"bulldog.mano" : 8269926853,
# "frankie.bullie" : 7919174863,
 # "_sullythebully_" : 8566172880,
"thorbullyboy" : 4294607348,
# "busterthebulldog17" : 7109283706,
# "milo_the_englishbulldog" : 6574408650,
#"bouba_the_english_bulldog" : 7702911218,
"rocco__the__bully" : 7628034507 # 4000 users
}

travelInstagramAccounts = {
"doounias" : 496065317,
"fursty" : 5514235,
"ryanresatka" : 233855716,
"jacob" : 927378976,
"everchanginghorizon" : 4035520,
"itsbigben" : 282574233,
"jackmartinphotoart" : 1325304121,
"alberthbyang" : 580302896,
"neohumanity" : 229748096,
"mydetoxtravel" : 196994193,
"huskysquad" : 982368547,
"erubes1" : 16584048,
"giuliogroebert" : 1664922478,
"rsyahrulhs" : 2104757633,
"sennarelax" : 14916676,
"eljackson" : 1118221,
"kitkat_ch" : 4670859,
"karl_shakur" : 183163798,
"mblockk" : 176236376,
"corrine_t" : 7025927,
"bokehm0n" : 230975865,
#"gozdepekin" : 24905203, 13000 users
"maxrivephotography" : 1671843770,
"ladzinski" : 11522830,
"amir_asani13" : 4976514062,
"wildtravelers" : 662247344
}

fitnessInstagramAccounts = {
"laceylivefit" : 29692719,
"minibutmighty_" : 2857895733,
"karinaelle" : 9136654,
"paigereilly" : 13521206,
"fearstofit" : 24273101,
"megandavis6" : 52251223,
"fit_and_dedicated" : 1533942699,
"shannon.henryy" : 1676629789,
"samanne.fit" : 1814854020,
"fitlifelucy" : 2956528105,
"mbpfitnesss" : 3261745074,
"presleykp.fit" : 1723030476,
"jasonpostonpro" : 30110648,
"cschmidt.fit" : 462505075,
"gymsharktrain" : 6975741036,
"gymsharkwomen" : 1659879703,
"gymshark" : 390927249
}

memeInstagramAccounts = {
"memes" : 300712527,
"instafootballmemes" : 1465387029,
"footballmemesinsta" : 1017415554,
"fuckyourchill" : 6979074440,
"theintrovertnation" : 4525144819,
"exoomf" : 8638359961,
"dreamsaboutmymemes" : 5682467752,
"gagfootball" : 4624712398,
"foot.beast" : 1101182287,
"goalnet433" : 4719477912,
"the.lad.football" : 3521965701,
"memesofootball" : 1967104341,
"footyemporium" : 446238634,
"iamfootballmemes" : 1799990133,
"thefutbolnet" : 2051036558
}

def getTimeDifference(start_time):
    difference = getDateNow() - start_time
    return difference.total_seconds()

def getInstagramAccount(instagramAccount):
    if instagramAccount == "models":
        accounts = modelsInstagramAccounts
    elif instagramAccount == "food":
        accounts = foodInstagramAccounts
    elif instagramAccount == "bulldogs":
        accounts = bulldogsInstagramAccounts
    elif instagramAccount == "travel":
        accounts = travelInstagramAccounts
    elif instagramAccount == "fitness":
        accounts = fitnessInstagramAccounts
    elif instagramAccount == "meme":
        accounts = memeInstagramAccounts
    else:
        print(str(getDateNow()) +" Unknown accounts, exiting")
        sys.exit()
    return accounts

def getTotalComments(api, media_id):

    comments = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getMediaCommentsUser(media_id, maxid=next_max_id)
        comments.extend(api.LastJson.get('comments', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return comments

def getTotalPopularFeed(api):
        popular_feed = []
        _ = api.getPopularFeed()
        #print(api.LastJson)
        #sys.exit()
        popular_feed.extend(api.LastJson.get('items', []))
        return popular_feed

def getMediaLikes(api, media_id):
    likes = []
    _ = api.getMediaLikers(media_id)
    likes = api.LastJson
    return likes

def getPublicFollowers(api,userId):
    publicFollowers = []
    counterPrivate = 0
    counterPublic = 0
    followers = api.getTotalFollowers(userId)
    print("followers", str(len(followers)) )
    for follower in followers:
        if follower['is_private'] == False:
            followersNotFollowing.append(follower)
    return publicFollowers


def getFollowersNotFollowing(api,userId):


    followersNotFollowing = []
    # counterPrivate = 0
    # counterPublic = 0
    myFollowers = api.getTotalFollowers(api.username_id)
    print(" (" + str(getDateNow()) + " myFollowers=" + str(len(myFollowers)) + ")")
    followers = api.getTotalFollowers(userId)
    print(str(getDateNow()) + " Source account followers", str(len(followers)))
    for follower in followers:
        # if follower['is_private'] == True:
        #     counterPrivate += 1
        # else:
        #     counterPublic += 1
        #print("this is the follower info: ", follower)
        beingFollowed = False
        for myFollower in myFollowers:
            if follower['pk'] == myFollower['pk']:
                beingFollowed = True
                break
        if beingFollowed == False:
            if follower['is_private'] == False:
                # followersNotFollowing.append(follower['pk'])
                followersNotFollowing.append(follower)
        # print("this is the follower info: ", follower)
            #print("follower id: " + str(follower['pk']) + "  Not equals following id " + str(myFollower['pk']))
        #print("this is the beinFollowed variable", str(beingFollowed) )
    print(str(getDateNow()) + " Size of list: ",len(followersNotFollowing))
    # print("counter private: ",str(counterPrivate))
    # print("counter public: ",str(counterPublic))
    print(str(getDateNow()) + " Just retrieved the followers not following")
    #print(followersNotFollowing)
    return followersNotFollowing

def getDateNow():
    return datetime.datetime.now()

def getMediaIdsFromUser(api,user):
    mediaIds = []
    userMediaIds = {}
    try:
        feed = getFeed(api,user['pk'])
        #print(str(getDateNow()) + " this is all the feed for user: " + str(user['username']) + " and user id: " + str(user['pk']) + " and the feed: " + str(feed))
    except KeyError as e:
        print(str(getDateNow()) + str(e))

    try:
        for f in feed:
            mediaIds.append(f['caption']['media_id'])
    except UnboundLocalError as e:
        print(str(getDateNow()) + str(e))
        pass
    except:
        #print(str(getDateNow()) + " Exception in f in feed loop")
        pass
            # print(str(getDateNow()) +"No media id for user: " + str(user['username']) + " with user_id: " + str(user['pk']))
    #print("this is media ids in the getmediaidsfromuser function after logic: ", mediaIds)
    userMediaIds['username'] = user['username']
    userMediaIds['pk'] = user['pk']
    userMediaIds['media_ids'] = mediaIds
    #print("this is the type of usermediaids ids: ", type(userMediaIds['media_ids']))
    return userMediaIds

def likeMedia(api,userMediaInfo):
    rmi = randomList(userMediaInfo['media_ids'])
    print(str(getDateNow()) +" Getting media item to like for username: "+ str(userMediaInfo['username']) + " with user_id: " + str(userMediaInfo['pk']) + " and mediaId " + str(rmi))
    likeResult = api.like(rmi)
    return likeResult

def likeMediaNew(api,media_id):
    likeResult = api.like(media_id)
    return likeResult

def getListRandomUsers(users,listSize):
    randomUsers = []
    while len(randomUsers) <= listSize:
        if len(randomUsers) <= 0:
            randomUsers.append(random.choice(users))
        else:
            ruser = random.choice(users)
            exists = False
            for ru in randomUsers:
                if ru['pk'] == ruser['pk']:
                    exists = True
                    break
            if exists == False:
                randomUsers.append(ruser)
    return randomUsers

def createCommentFromUserList(users):
    print users
    comment = ""
    for user in users:
        comment += " @" + user['username']
    comment += " :) :)"
    return comment

def randomComment():
    # comments = ["Nice :)", "Wow :)", "Cool :)", "Awesome :)"]
    comments = ["❤️❤️❤️","sweet :)","Nice :)", "Wow :)", "Cool :)", "Awesome :)"]
    comment = randomList(comments)
    return comment

def commentMedia(api,media_id,comment):
    commentResult = api.comment(media_id,comment)
    return commentResult

def mediaHasBeenLiked(api,media_id):
    total_likes = getMediaLikes(api,media_id)
    hasBeenLiked = False
    for user in total_likes['users']:
        if user['username'] == api.username:
            print(str(getDateNow()) +" User has liked media, ruling out media")
            hasBeenLiked = True
    return hasBeenLiked

def mediaHasBeenCommented(api,media_id):

    total_comments = getTotalComments(api,media_id)
    hasBeenCommented = False
    for comment in total_comments:
        # print comment['user']['username']
        if comment['user']['username'] == api.username:
            print(str(getDateNow()) +" User has commented, ruling out media")
            hasBeenCommented = True
    return hasBeenCommented


def getFeed(api,user_id):
    feed = api.getTotalUserFeed(user_id)
    return feed

def prettyJson(data):
    return json.dumps(data, indent=4, sort_keys=True)

def getFollowersToUnfollow(api,user_id):
    followersToUnfollow = []
    followers = api.getTotalFollowers(api.username_id)
    followings = api.getTotalFollowings(api.username_id)
    print("followers", str(len(followers)) )
    print("followings", str(len(followings)) )
    for follower in followers:
        beingFollowed = False
        for following in followings:
            if follower['pk'] == following['pk']:
                beingFollowed = True
                break
        if beingFollowed == True:
            followersToUnfollow.append(follower['pk'])
    print("size of list: ",len(followersToUnfollow))
    print(str(getDateNow()) + " Just retrieved the followings to unfollow")
    return followersToUnfollow

def randomNumber(firtNumber,lastNumber):
    return random.randint(firtNumber,lastNumber)

def randomNumberWithLimit(limit,list):
    rnf = 0
    rn = random.randint(0,len(list))
    if (rn + limit) > len(list):
        rnf = len(list) - limit
    elif rn - limit < 0:
        rnf = 0
    else:
        rnf = rn
    return rnf

def randomDict(dict):
    insAc = random.choice(dict.keys())
    return insAc

def randomList(list):
        return random.choice(list)

def followUser(user):
    fll = api.follow(user['pk'])
    print(str(getDateNow()) + " Username: " + str(user['username'])  + " UserID: " + str(users['pk']) + " is: " + str(fll))
    return fll

def writeInFile(path_to_file,text):
    with open(path_to_file, 'w+') as f:
        f.write(text)
    print "just written in file"
    f.close()

def unfollowUsers(users):
    counter = 0
    sleeping = 600
    for u in users:
        unfll = api.unfollow(u)
        if unfll == False:
            print("Exiting script action to unfollow has returned False")
            logout()
        print(str(getDateNow()) + " UserID: " + str(u) + " is: " + str(unfll))
        counter += 1
        sleep(5)

def logout(api):
    api.logout()

def getUsersIds(users):
    for x in list:
        print x['username'],x['pk']

def getRandomSleep(first,last):
    sleepPair = {'first': first,'last': last }
    return sleepPair
