from bs4 import BeautifulSoup
from kidwrit import kidparser
from kidwrit import kid_logging

# making directory for log files
log_dir = logging.log_directory()

# opening our file
with open('kids_full.html', "r") as f:
    # splitting the file by h1 tags: each part contains kid+texts
    h1_blocks = kidparser.toss_block(f.readline(), 'h1')

    for h1_block in h1_blocks:
        # separate the block into h1 (kid) and h2 (texts)
        tossed_h1 = kidparser.toss_block(h1_block, '/h1>')
        # parse kid info from h1
        kid = kidparser.parse_kid(BeautifulSoup(tossed_h1[0], 'html.parser'))
        # LATER WE'LL CALCULATE KID'S GRADE HERE
        # write it to log
        log = logging.Logfile(kid.name, log_dir)
        log.mk_note(kid.to_string())
        # h1_soup = BeautifulSoup(tossed_h1[1], 'html.parser')

        h2_blocks = kidparser.toss_block(tossed_h1[1], 'h2')

        for h2_block in h2_blocks:
            # separate the block into h2 (heading) and s (text)
            tossed_h2 = kidparser.toss_block(h2_block, '/h2>')
            # make a text template from heading info from h2
            texts = kidparser.parse_texts(BeautifulSoup(tossed_h2[0], 'html.parser'), kid)
            # make a note to log, ofc
            for t in texts: log.mk_note(t.to_string())
