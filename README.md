# Game schedule generation script for LAN parties

Record game votes in `votes.json` and then run `./game-scheduler.py`.

## Algorithm

Based on the votes data, a list of game choices is created, with games that
receive multiple votes appearing multiple times in the list. Then an empty
schedule list is created, and games are randomly selected from the game choices
list.

If a game receives more votes, it's more likely to appear earlier on the list,
and therefore will be more likely to be played, but there is an element of
randomness that introduces variety.

## Configuration

Example `votes.json`:
```
{
    "Game A": 5,
    "Game B": 10,
    "Game C": 1
}
```
