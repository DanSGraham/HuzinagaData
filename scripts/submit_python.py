#! /usr/bin/env python

#TODO: Allow any order of args, change outputfile format
from __future__ import print_function
import argparse
import os

def main():
    '''The main program.'''
    from os.path import expanduser, expandvars, abspath, splitext
    from os.path import isfile, getmtime
    from os import chmod
    from subprocess import call
    import datetime

    opts = arguments()

    # Submit each file
    for f in opts.files:
        file_path = opts.directory + f
        absfile = abspath(expandvars(expanduser(file_path)))
        abserr = splitext(absfile)[0] + '.err'
        abslog = splitext(absfile)[0] + '.log'
        absout = splitext(absfile)[0] + '.out'
        fpbs = splitext(absfile)[0] + '.pbs'
        prenom = file_path.split('.')[0]

        # if log/error/output files already exist, move them
        for oldfile in [abserr, abslog, absout]:
            if isfile(oldfile):
                d = datetime.datetime.fromtimestamp(getmtime(oldfile))
                newfile = oldfile+'.{0:02d}-{1:02d}-{2:04d}_{3:02d}:{4:02d}:{5:02d}'.format(
                          d.month, d.day, d.year, d.hour, d.minute, d.second)
                call (['mv', oldfile, newfile])

        # generate pbs file
        pbsfile = open(fpbs, 'w')
        print ('#!/bin/bash', file=pbsfile)
        print ('#PBS -N {0}'.format(f[:-4]), file=pbsfile)
        print ('#PBS -l nodes={0}:ppn={1}'.format(opts.nodes, opts.ppn), file=pbsfile)
        print ('#PBS -l walltime={0}'.format(opts.wall), file=pbsfile)
        print ('#PBS -l pmem={0}mb'.format(opts.mem), file=pbsfile)
        if opts.scratch == 'ssd':
            print ('#PBS -l ssd', file=pbsfile)
#        print ('#PBS -M {0}@umn.edu'.format(opts.user), file=pbsfile)
        print ('#PBS -e {0}'.format(abserr), file=pbsfile)
        print ('#PBS -o {0}'.format(abslog), file=pbsfile)
        print ('#PBS -q {0}'.format(opts.queue), file=pbsfile)
        print ('', file=pbsfile)
        print ('module load python', file=pbsfile)
#        print ('cd ${PBS_O_WORKDIR}', file=pbsfile)
#        print ('', file=pbsfile)

        # create scratch directory to work in
        print ('# create scratch directory', file=pbsfile)
        if opts.scratch == 'ram':
            print ('scratch=/dev/shm/SWR/{0}/{1}'.format(opts.user, prenom), file=pbsfile)
        elif opts.scratch == 'local':
            print ('scratch=/scratch.local/{0}/{1}'.format(opts.user, prenom), file=pbsfile)
        elif opts.scratch == 'ssd':
            print ('scratch=/scratch.ssd/{0}/{1}'.format(opts.user, prenom), file=pbsfile)
        else:
            print ('scratch=/scratch.global/{0}/{1}'.format(opts.user, prenom), file=pbsfile)

        print ('if [[ -d $scratch ]]; then', file=pbsfile)
        print ('    i=0', file=pbsfile)
        print ('    while [[ -d $scratch-$i ]]; do', file=pbsfile)
        print ('        let i++', file=pbsfile)
        print ('    done', file=pbsfile)
        print ('    scratch=$scratch-$i', file=pbsfile)
        print ('fi', file=pbsfile)

        print ('rm -rf $scratch 2> /dev/null', file=pbsfile)
        print ('mkdir -p $scratch', file=pbsfile)
        print ('cd $scratch', file=pbsfile)
        print ('', file=pbsfile)

        # submit file, clean up scratch dir
        print ('python {0} {1} > {2}'.format(opts.code, absfile, absout), file=pbsfile)
        print ('', file=pbsfile)
        print ('cd ${PBS_O_WORKDIR}', file=pbsfile)
        print ('rm -rf $scratch 2> /dev/null', file=pbsfile)
        pbsfile.close()

        # make script executable
        chmod(fpbs, 0o755)

        # submit file to queue
        if not opts.script:
            call(['qsub', fpbs])

class options():
    '''An options class to hold all the possible options.'''

    def __init__(self):
        self.code      = None
        self.nodes     = None
        self.ppn       = None
        self.mem       = None
        self.wall      = None
        self.user      = None
        self.files     = None
        self.directory = None
        self.script    = False
        self.queue     = None


# Allow input of directories
#http://stackoverflow.com/questions/11415570/directory-path-types-with-argparse
class readable_dir(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):

        prospective_dir = values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)

        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))


def arguments():
    '''Gets the options based on the arguments passed in.'''

    from argparse import ArgumentParser, RawDescriptionHelpFormatter
    from textwrap import dedent
    import sys
    from os import environ

    parser = ArgumentParser(description=dedent(main.__doc__),
                            formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument('input_files', nargs='*', default=sys.stdin,
                        help='The input files to submit.')
    parser.add_argument('-c', '--code', help='The python code you wish to run.')
    parser.add_argument('-n', '--nodes', help='The number of nodes to run on.',
                        type=int)
    parser.add_argument('-p', '--ppn', help='The processors per node to use.',
                        type=int)
    parser.add_argument('-w', '--wall', help='The wall time to request in any '
                        'of: sec, min:sec, hour:min:sec, day:hour:min:sec.',
                        metavar='WALLTIME')
    parser.add_argument('-m', '--mem', help='Request a particular amount of '
                        'memory per processor. Given in MB.', type=int)
    parser.add_argument('-a', '--all', help='Specify nodes, ppn, wall and mem '
                        'with a single option, in that order.  i.e. '
                        '--all 8 1 48:00:00 2000 for 8 nodes, 1 ppn, '
                        '48:00:00 walltime and 2000MB. ', nargs=4,
                        metavar=('NODES', 'PPN', 'WALLTIME', 'MEM'))
    parser.add_argument('-q', '--queue', help='The MESABI queue to submit to. '
                        'Available queues are: mesabi (default), small, large, '
                        'widest, max, ram256, ram1t, or k40', default='mesabi')
    parser.add_argument('-x', '--scratch', help='Specify what to use as the scratch folder. '
                        'Defaults to scratch.global', default='global')
    parser.add_argument('-s', '--script', help='Create the PBS script only. '
                        'Does not submit to queue. Default FALSE.',
                        action='store_true', default=False)
    parser.add_argument('-d', '--directory', help='A directory which contains '
                        'the .inp files to submit. Serves as an alternative to individual '
                        ' files.', action=readable_dir)

    args = parser.parse_args()

    # Initialize options
    opts = options()
    opts.user = environ['USER']
    opts.script = args.script
    opts.queue = args.queue.lower()
    opts.scratch = args.scratch.lower()

    # get python code to run
    if args.code is not None:
        opts.code = args.code
    else:
        opts.code = ''

    # Get number of nodes
    if args.nodes is not None:
        opts.nodes = args.nodes
    elif args.all is not None:
        opts.nodes = int(args.all[0])
    else:
        st = 'How many nodes do you want assigned? [1] '
        opts.nodes = input(st)
        if not opts.nodes: opts.nodes = 1

    # Get PPN
    if args.ppn is not None:
        opts.ppn = args.ppn
    elif args.all is not None:
        opts.ppn = int(args.all[1])
    else:
        st = 'How many processors per node? [8] '
        opts.ppn = input(st)
        if not opts.ppn: opts.ppn = 8

    # Get walltime
    if args.wall is not None:
        opts.wall = args.wall
    elif args.all is not None:
        opts.wall = args.all[2]
    else:
        st = 'Requested wall close time? [8:00:00] '
        opts.wall = input(st)
        if not opts.wall: opts.wall = '8:00:00'

    # Get memory
    if args.mem is not None:
        opts.mem = args.mem
    elif args.all is not None:
        opts.mem = int(args.all[3])
    else:
        st = 'How much memory per processor do you want (MB) [2000] '
        opts.mem = input(st)
        if not opts.mem: opts.mem = 2000

    if args.directory is not None:
        any_inp_files = False
        opts.directory = args.directory
        opts.files = []
        for filename in os.listdir(args.directory):
            if filename.endswith(".inp"): #only submits .inp files
                opts.files.append(filename)
                any_inp_files = True

        if not any_inp_files:
            print ("No .inp files in the folder")
    else:
        opts.directory = ""
        opts.files = args.input_files[:]

    return opts

if __name__=='__main__':
    '''The main program.'''

    main()
