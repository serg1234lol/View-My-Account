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
    attempt = 0
    break_counter = 0
    start_time = getDateNow()
    elapsed_time = 0
    TOTAL_TIME = 4500 # seconds
    while counter <= TOTAL_COMMENTS:
    #while True:
    #while elapsed_time <= TOTAL_TIME:
        if elapsed_time >= TOTAL_TIME:
            print(str(getDateNow()) + " Exiting because Elapsed time: " + str(elapsed_time)
            + " is over total time: " + str(TOTAL_TIME))
            logout(api)
            sys.exit()
        while True:
            try:
                user = random.choice(newFollowers)
                media = getMediaIdsFromUser(api,user)
                attempt += 1
                #print(str(getDateNow()) + " len of media: ", str(len(media['media_ids'])))
                # if len(media['media_ids']) > 0:
                #     rmi = randomList(media['media_ids'])
                #     if mediaHasBeenCommented(api,rmi) == False:
                #         break
                # else:
                #     continue
                if len(media['media_ids']) > 0:
                    foundId = False
                    for id in media['media_ids']:
                    #rmi = randomList(media['media_ids'])
                        if mediaHasBeenCommented(api,id) == False:
                            #print "media has NOT been liked"
                            foundId = True
                            rmi = id
                            break
                        #print "media has been liked"
                    if foundId == True:
                        break
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
        #print comment
        resp = commentMedia(api,rmi,comment)
        if resp == True:
            print(str(getDateNow()) +" Getting media item to comment for username: "
            + str(media['username']) + " with user_id: " + str(media['pk'])
            + " and mediaId " + str(rmi) + " and comment: " + str(comment))
            counter += 1
            rs = getRandomSleep(350,400)
            rn = randomNumber(rs['first'],rs['last'])
            print(str(getDateNow()) + " Sleeping now with seconds: " + str(rn)
            +  ", this is the counter until total comments: " + str(counter)
            + " and total comment attempts: " + str(attempt))
            elapsed_time = getTimeDifference(start_time)
            print(str(getDateNow()) + " Elapsed time: " + str(elapsed_time)
            + " and total time: " + str(TOTAL_TIME))
            sleep(rn)
        else:
            print(str(getDateNow()) + " Response for comment returned False")
            break_counter +=1
            if break_counter >= 1:
                print(str(getDateNow()) + " Exiting script as like resp is False few times")
                logout(api)
                sys.exit()
    logout(api)
