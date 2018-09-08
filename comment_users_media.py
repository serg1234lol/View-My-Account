#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from InstagramApiExtended import *

credentials = sys.argv[1]
instaAccounts = sys.argv[2]

accounts = getInstagramAccount(instaAccounts)

if __name__ == "__main__":
    cfg = load_config(credentials)
    api = InstagramAPI(cfg.user, cfg.password)
    api.login()

    rk = randomDict(accounts)
    ia = accounts[rk]
    print(str(getDateNow()) + " random account to get the followers: ", rk)
    newFollowers = getFollowersNotFollowing(api,ia)
    TOTAL_COMMENTS = 12
    counter = 0
    break_counter = 0
    while counter <= TOTAL_COMMENTS:
        while True:
            try:
                user = random.choice(newFollowers)
                media = getMediaIdsFromUser(api,user)
                print(str(getDateNow()) + " len of media: ", str(len(media['media_ids'])))
                if len(media['media_ids']) > 0:
                    rmi = randomList(media['media_ids'])
                    if mediaHasBeenCommented(api,rmi) == False:
                        break
                else:
                    continue
            except IndexError as ie:
                pass
                # print(str(getDateNow()) + str(ie))
            except NameError as ne:
                print(str(getDateNow()) + "Exception: " + str(ne))
                logout(api)
                sys.exit()
                break
            except:
                print(str(getDateNow()) + " Exception trying to get media")
        randomUsers = getListRandomUsers(newFollowers,3)
        comment = randomComment()
        print comment
        resp = commentMedia(api,rmi,comment)
        if resp == True:
            print(str(getDateNow()) +" Getting media item to commment for username: "+ str(media['username']) + " with user_id: " + str(media['pk']) + " and mediaId " + str(rmi))
            counter += 1
            rs = getRandomSleep(350,400)
            rn = randomNumber(rs['first'],rs['last'])
            print(str(getDateNow()) + " Sleeping now with seconds: " + str(rn) +  ", this is the counter until comments: " + str(counter))
            sleep(rn)
        else:
            print(str(getDateNow()) + " Response for comment returned False")
            break_counter +=1
            if break_counter >= 1:
                print(str(getDateNow()) + " Exiting script as like resp is False few times")
                logout(api)
                sys.exit()
    logout(api)
