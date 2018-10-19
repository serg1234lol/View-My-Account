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
    TOTAL_LIKES = 70
    counter = 0
    like_attempt = 0
    break_counter = 0
    start_time = getDateNow()
    elapsed_time = 0
    TOTAL_TIME = 5400 # seconds
    while counter <= TOTAL_LIKES:
    #while True:
    #while elapsed_time <= TOTAL_TIME:
        if elapsed_time >= TOTAL_TIME:
            print(str(getDateNow()) + " Exiting because Elapsed time: " + str(elapsed_time)
            + " is over total time: " + str(TOTAL_TIME))
            logout(api)
            sys.exit()
        while True:
            #print "beginning of second while loop"
            try:
                user = random.choice(newFollowers)
                tried_user = 0;
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
                        tried_user += 1
                        if tried_user > 3:
                            print(str(getDateNow()) + "User: " + str(user['username'])
                            + " attempts to like: " + str(tried_user))
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
            print(str(getDateNow()) +" Getting media-item to like for username: "
            + str(media['username']) + " with user_id: " + str(media['pk'])
            + " and mediaId " + str(rmi))
            counter += 1
            rs = getRandomSleep(63,73)
            rn = randomNumber(rs['first'],rs['last'])
            print(str(getDateNow()) + " Sleeping now with seconds: " + str(rn)
            +  ", this is the counter until total likes: " + str(counter)
            + " and total like attempts: " + str(like_attempt))
            elapsed_time = getTimeDifference(start_time)
            print(str(getDateNow()) + " Elapsed time: " + str(elapsed_time)
            + " and total time: " + str(TOTAL_TIME))
            sleep(rn)
        else:
            print(str(getDateNow()) + " Response for like returned False")
            break_counter +=1
            if break_counter >= 1:
                print(str(getDateNow()) + " Exiting script as like resp is False few times")
                logout(api)
                sys.exit()
    logout(api)
