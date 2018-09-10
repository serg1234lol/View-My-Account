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
    TOTAL_LIKES = 55
    counter = 0
    like_attempt = 0
    break_counter = 0
    start_time = getDateNow()
    elapsed_time = 0
    TOTAL_TIME = 4500 # seconds
    # while counter <= TOTAL_LIKES:
    while elapsed_time <= TOTAL_TIME:
        while True:
            #print "beginning of second while loop"
            try:
                user = random.choice(newFollowers)
                media = getMediaIdsFromUser(api,user)
                like_attempt += 1
                #print("size of media: " + str(len(media['media_ids'])))
                if len(media['media_ids']) > 0:
                    foundId = False
                    for id in media['media_ids']:
                    #rmi = randomList(media['media_ids'])
                        if mediaHasBeenLiked(api,id) == False:
                            #print "media has NOT been liked"
                            foundId = True
                            rmi = id
                            break
                        #print "media has been liked"
                    if foundId == True:
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
            # except:
            #     print(str(getDateNow()) + " Exception trying to get media")
        resp = likeMediaNew(api,rmi)
        if resp == True:
            print(str(getDateNow()) +" Getting media item to like for username: "
            + str(media['username']) + " with user_id: " + str(media['pk'])
            + " and mediaId " + str(rmi))
            counter += 1
            rs = getRandomSleep(61,71)
            rn = randomNumber(rs['first'],rs['last'])
            print(str(getDateNow()) + " Sleeping now with seconds: " + str(rn)
            +  ", this is the counter until total likes: " + str(counter)
            + " and total like attempts: " + str(like_attempt))
            elapsed_time = getTimeDifference(start_time)
            print(str(getDateNow()) + " Elapsed time: " + str(elapsed_time)
            + " and total time: " + str(TOTAL_TIME))
            sleep(rn)
            # if elapsed_time >= TOTAL_TIME:
            #     print(str(getDateNow()) + " Elapsed time: " + str(elapsed_time)
            #     + " bigger than total time: " + str(TOTAL_TIME))
            #     logout(api)
            #     sys.exit()
            #print("this is the elapsed time: " + str(elapsed_time))

        else:
            print(str(getDateNow()) + " Response for like returned False")
            break_counter +=1
            if break_counter >= 2:
                print(str(getDateNow()) + " Exiting script as like resp is False few times")
                logout(api)
                sys.exit()
    logout(api)
