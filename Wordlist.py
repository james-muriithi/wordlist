import itertools
import time
import math
import optparse
import os


def wordlist(minimum, maximum, characters, outputfile):
    maximum = int(maximum)
    minimum = int(minimum)
    if maximum >= minimum:
        if os.path.dirname(outputfile):
            if not os.path.exists(os.path.dirname(outputfile)):
                os.makedirs(os.path.dirname(outputfile))

        file = open(outputfile, 'w')
        print "[+] creating wordlist..."
        start = time.clock()
        starting_time = time.strftime('%H:%M:%S')
        print "[i] starting time %s" % starting_time
        character_length = len(str(characters))
        if minimum == maximum:
            total_passwords = character_length ** minimum
        else:
            total_passwords = character_length ** minimum + character_length ** maximum

        print str(total_passwords) + " passwords"
        for i in range(minimum, maximum + 1):
            for xs in itertools.product(str(characters), repeat=i):
                file.write(''.join(xs) + "\n")

        file.close()
        stoping_time = time.strftime('%H:%M:%S')
        stop = time.clock()
        print "[i] stoping time %s" % stoping_time
        sec = math.ceil(int(stop - start))
        print "Elapsed time: %s seconds" % sec
    else:
        print "Check your minimum and maximum values please"


def main():
    parser = optparse.OptionParser("--min <minimum pass length> --max <maximum pass length>"
                                   " --c <combination> --o <output.ext>")
    parser.add_option('--min', dest='minimum', type='string',
                      help='the minimum password length')
    parser.add_option('--max', dest='maximum', type='int',
                      help='the maximum password length')
    parser.add_option('--c', dest='combination', type='string',
                      help='the combination of numbers eg. 1234')
    parser.add_option('--o', dest='output_file', type='string',
                      help='the maximum password length')
    (options, arg) = parser.parse_args()
    if (options.minimum == None) or (options.maximum == None) or options.combination == None or options.output_file == None:
        print parser.usage
        exit(0)
    else:
        minimum = options.minimum
        maximum = options.maximum
        combination = options.combination
        output_file = options.output_file
        wordlist(minimum, maximum, combination, output_file)


if __name__ == '__main__':
    main()
