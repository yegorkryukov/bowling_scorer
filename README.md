# Bowling Game Coding Exercise 

Create a program, which, given a valid sequence of throws for one game of American Ten-Pin Bowling, produces the total score for the game​. ​Your code will become the core of a bowling score management system, so make sure it fully complies with the input and output requirements, and represents your best code.

1. **[scorer.py](https://github.com/yegorkryukov/bowling_scorer/blob/master/scorer.py)** : main program
2. **[tests.py](https://github.com/yegorkryukov/bowling_scorer/blob/master/tests.py)**  : unittests
3. [Docker image](https://cloud.docker.com/u/iopheam/repository/docker/iopheam/bowling_scorer) ![]() 

## How to run
### Python
Run **scorer.py** with no arguments:
```bash
~$ python scorer.py 
Enter the sequence to evaluate: 
45-54-36-27-09-63-81-18-90-72
Score: 90
```
or pass the sequence when calling the scorer:
```bash
~$ python scorer.py 45-54-36-27-09-63-81-18-90-72
Sequence: 45-54-36-27-09-63-81-18-90-72, score: 90
```

### Docker

Run docker container without arguments and the program will ask you to enter the sequence:

```bash
~$ docker run --tty --interactive iopheam/bowling_scorer:V1
V1: Pulling from iopheam/bowling_scorer
...
Status: Downloaded newer image for iopheam/bowling_scorer:V1
Enter the sequence to evaluate:
45-54-36-27-09-63-81-18-90-72
Score: 90
```

or pass the sequence to evaluate in command line:
```bash
~$ docker run --tty --interactive iopheam/bowling_scorer:V1 45-54-36-27-09-63-81-18-90-72
Sequence: 45-54-36-27-09-63-81-18-90-72, score: 90
```


