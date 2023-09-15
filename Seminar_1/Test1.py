import subprocess
import string



if __name__ == '__main__':

    def print_text(operation, text, word):

        result = subprocess.run(f'{operation}, "{text}"', shell=True, stdout=subprocess.PIPE, encoding='utf-8')


        out = result.stdout.translate(str.maketrans("", "", string.punctuation))


        if word in out:
            return True
        else:
            return False



print(print_text('echo', 'one, two, three, four.', 'five'))
