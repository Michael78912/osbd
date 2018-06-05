class MarkupFile:
    def __init__(self, data):
        self.data = data
        self.parse()

    def parse(self):
        raw = self.data.split('\n')
        no_comments = []
        for line in raw:
            line += line.split('#')[0]

        in_block_comment = False
        no_block_comments = []

        for line in no_comments:
            if '#(' in line:
                in_block_comment = True
                line = line.split('#(')[0]

            if in_block_comment:
                if ')#' in line:
                    in_block_comment = False
                    line = line.split(')#')[1]

            no_block_comments.append(line)

        return no_block_comments
