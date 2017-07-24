def open_file():
    fp = open('player_career.csv')
    dummy = fp.readline()
    players = []
    for oku in fp:
        sp = oku.split(",")
        oyuncu = [sp[0], sp[1], sp[2], sp[3], int(sp[4]), int(sp[5]), int(sp[6]), sp[7], sp[8], int(sp[9]), sp[10],
                  sp[11], sp[12], sp[13], sp[14], sp[15], sp[16], int(sp[17]), sp[18], sp[19], sp[20]]
        players.append(oyuncu)
    return players


def dosya_yaz(eff):
    fp = open('top50.txt', 'w')
    for i in range(50):
        string = "" + eff[i][0] + " " + eff[i][1] + " " + str(eff[i][2]) + "\n"
        fp.write(string)


def main():
    players = open_file()
    eff = []
    for i in range(len(players)):
        efficiency = (
            ((int(players[i][6]) + int(players[i][9]) + int(players[i][10]) + int(players[i][11]) + int(players[i][12]))
             - ((int(players[i][15]) - int(players[i][16])) + (int(players[i][17]) - int(players[i][18])) + int(
                players[i][13]))) / int(players[i][4]))
        temp = [players[i][1], players[i][2], efficiency]
        eff.append(temp)
    eff.sort(key=lambda den: den[2], reverse=True)
    dosya_yaz(eff)

    players.sort(key=lambda dup: dup[5], reverse=True)
    print("Longest Time Played:", players[0][1], players[0][2], ",", players[0][5])
    players.sort(key=lambda dup: dup[4], reverse=True)
    print("Most Game Played:", players[0][1], players[0][2], ",", players[0][4])
    players.sort(key=lambda dup: dup[6], reverse=True)
    print("Most Points Scored:", players[0][1], players[0][2], ",", players[0][6])
    players.sort(key=lambda dup: dup[9], reverse=True)
    print("Most Rebounds:", players[0][1], players[0][2], ",", players[0][9])
    players.sort(key=lambda dup: dup[17], reverse=True)
    print("Most Free throws:", players[0][1], players[0][2], ",", players[0][17])


if __name__ == '__main__':
    main()
