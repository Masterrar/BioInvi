import sys
import getopt
import Domain.UseCase.File.EditFile as FileUseCases
import Data.FastaWorker as FastaWorker
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    ara = FastaWorker.FastaWorker("C:\\Users\\Alex\\PycharmProjects\\BioInvi\\TestData\\MUSCLE_species5_consensus_03_copy1.fasta")
    print(ara.fastaList)
    '''
    ara.ReplaceSeq(1,3)
    print(ara.fastaList)
    '''
    ara.SplitFile(2)
    print(ara.fastaList)

if __name__ == "__main__":
    sys.exit(main())