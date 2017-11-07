class FastaWorker:
    fastaList = []

    def __init__(self):
        self
    def __init__(self, path):
        self.OpenSeqFile(path)
        self

    def OpenSeqFile(self, path):
        i = 0
        self.pathToFile = path
        with open(path, "rU") as handle:
            line = handle.readline()
            lineSeq = line
            while(handle.closed == False):
                if(line.isspace() or line == "" or line==" "):
                    break
                if(line[0] == ">"):
                    while(handle.closed == False):
                        i = i + 1
                        print(str(handle.closed) + str(i))
                        lineSeq = handle.readline()
                        if (lineSeq.isspace() or lineSeq == "" or lineSeq == " "):
                            handle.close()
                            break
                        if ( lineSeq[0] == ">" or handle.readable() == False):
                            line = lineSeq
                            break
                        self.fastaList.append((i,line,lineSeq))

    def ReplaceSeq(self,fromN, toN):
        needSeq = self.fastaList.pop(fromN)
        self.fastaList.insert(toN,needSeq)
        with open(self.pathToFile, "w") as handle:
            for seq in self.fastaList:
                handle.write(seq[1] + seq[2])

    def SplitFile(self,splitN):
        count = self.fastaList.__len__()
        self.SplitFileRange(splitN,count)

    def SplitFileRange(self, nFrom, nTo):
        needSplitSeq = []
        rangeSplit = range(nFrom,nTo)
        k = nFrom
        for i in rangeSplit:
            needSplitSeq.append(self.fastaList.pop(k))
        with open(self.pathToFile + "out", "w") as handle:
            for seq in needSplitSeq:
                handle.write(seq[1] + seq[2])




