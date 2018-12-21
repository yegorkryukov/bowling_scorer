FROM python:3
ADD scorer.py /
ENTRYPOINT [ "python", "./scorer.py" ]


