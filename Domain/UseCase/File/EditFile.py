from Bio import SeqIO

class FileUseCases:
    TFFasta = "fasta"
    pathToFile = None
    fileStream = None

    def OpenSeqFile(self, path):
        self.pathToFile = path
        with open(path, "rU") as handle:
            self.fileStream = handle

            for record in SeqIO.parse(handle, self.TFFasta):
                print(record.id)

    def ReplaceSeq(self, idStr, toNum):
        print("ReplaceSeq. Было.")

        with open(self.pathToFile, "rU") as handle:
            for record in SeqIO.parse(handle, self.TFFasta):
                print(record.id)

            file = SeqIO.parse(handle, self.TFFasta)
            print(file[idStr].id)
            ara = file.pop(idStr)
            file.insert(toNum,ara)
            print("ReplaceSeq. Стало.")
            for record in SeqIO.parse(self.fileStream, self.TFFasta):
                print(record.id)
            print("ReplaceSeq. В массиве")
            for record in file:
                print(record.id)








