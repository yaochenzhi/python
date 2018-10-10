def locate(value, rise=None, down=None):
    # rise = ([value_list], [location_list])
    if rise:
        if value >= rise[0][0]:

            for index, limit in enumerate(rise[0]):
                if value >= rise[0][index]:
                    if index < ( len(rise[0]) - 1 ):
                        if value < rise[0][index+1]:
                            return rise[1][index]
                    else:
                        return rise[1][index]
    if down:
        if value <= down[0][0]:

            for index, limit in enumerate(down[0]):
                if value <= down[0][index]:
                    if index < ( len(down[0]) - 1 ):
                        if value > down[0][index+1]:
                            return down[1][index]
                    else:
                        return down[1][index]
                        
                        
if __name__ == "__main__":

    location = locate(71, rise=((40, 50, 70), (1, 2, 3)))

    print(location)

    location = locate(70, down=((90, 80, 70), (1, 2, 3)))

    print(location)
